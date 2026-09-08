// Keep the dashboard pointed at the file produced by the ETL run.
const DATA_URL = "data/processed/dashboard.json";
const INCOME_CATEGORIES = new Set(["deposit", "income", "credit"]);
let dashboardData = [];

async function loadDashboardData() {
    setLoadingState(true);
    try {
        const response = await fetch(`${DATA_URL}?t=${Date.now()}`);
        if (!response.ok) {
            throw new Error(`Data request failed with status ${response.status}`);
        }
        const data = await response.json();
        dashboardData = Array.isArray(data) ? data : [];
        renderDashboard(dashboardData);
    } catch (err) {
        console.error("Could not load dashboard data:", err);
        renderErrorState();
    } finally {
        setLoadingState(false);
    }
}

function renderDashboard(data) {
    renderSummary(data);
    renderCategories(data);
    renderTable(data);
    renderSignal(data);
    renderReportingWindow(data);
}

function renderSummary(data) {
    const moneyIn = data.filter(isIncome).reduce((sum, txn) => sum + amountOf(txn), 0);
    const moneyOut = data.filter(txn => !isIncome(txn)).reduce((sum, txn) => sum + amountOf(txn), 0);
    const categoryCounts = getCategoryCounts(data);
    const top = categoryCounts[0];

    document.getElementById("total-transactions").textContent = data.length;
    document.getElementById("money-in").textContent = formatAmount(moneyIn);
    document.getElementById("money-out").textContent = formatAmount(moneyOut);
    document.getElementById("top-category").textContent = top ? top.name : "None";
    document.getElementById("top-category-note").textContent = top ? `${top.count} of ${data.length} records` : "No records yet";
}

function renderCategories(data) {
    const list = document.getElementById("category-list");
    const categoryCounts = getCategoryCounts(data);
    document.getElementById("category-count").textContent = `${categoryCounts.length} categories`;

    if (!categoryCounts.length) {
        list.innerHTML = '<p class="empty-state">No category data available yet.</p>';
        return;
    }

    const maxCount = categoryCounts[0].count;
    list.innerHTML = categoryCounts.map(category => `
        <div class="category-row">
            <span class="category-name">${escapeHtml(category.name)}</span>
            <div class="category-bar" aria-label="${category.count} transactions">
                <span style="width: ${(category.count / maxCount) * 100}%"></span>
            </div>
            <span class="category-total">${category.count} record${category.count === 1 ? "" : "s"}</span>
        </div>
    `).join("");
}

function renderTable(data, query = "") {
    const tbody = document.querySelector("#txn-table tbody");
    const normalizedQuery = query.trim().toLowerCase();
    const filtered = data.filter(txn => [txn.date, txn.category, txn.amount].join(" ").toLowerCase().includes(normalizedQuery));
    tbody.innerHTML = filtered.length ? filtered.map(transactionRow).join("") : '<tr><td class="empty-state" colspan="4">No matching transactions found.</td></tr>';
    document.getElementById("table-status").textContent = `${filtered.length} of ${data.length} records shown`;
}

function transactionRow(txn) {
    const category = String(txn.category || "other").toLowerCase();
    const direction = isIncome(txn) ? "In" : "Out";
    return `
        <tr>
            <td class="date-cell">${escapeHtml(formatDate(txn.date))}</td>
            <td class="amount-cell">${formatAmount(amountOf(txn))}</td>
            <td><span class="category-tag">${escapeHtml(category)}</span></td>
            <td class="direction ${direction === "In" ? "in" : "out"}">${direction}</td>
        </tr>
    `;
}

function renderSignal(data) {
    const message = document.getElementById("signal-message");
    if (!data.length) {
        message.textContent = "Add processed records to reveal a pattern.";
        return;
    }
    const categoryCounts = getCategoryCounts(data);
    const leader = categoryCounts[0];
    message.textContent = `${capitalize(leader.name)} leads the ledger with ${leader.count} record${leader.count === 1 ? "" : "s"}.`;
}

function renderReportingWindow(data) {
    const dates = data.map(txn => new Date(txn.date)).filter(date => !Number.isNaN(date.getTime())).sort((a, b) => a - b);
    const window = document.getElementById("reporting-window");
    if (!dates.length) {
        window.textContent = "No dated records";
        return;
    }
    const formatter = new Intl.DateTimeFormat("en", { month: "short", day: "numeric", year: "numeric" });
    window.textContent = dates.length === 1 ? formatter.format(dates[0]) : `${formatter.format(dates[0])} - ${formatter.format(dates[dates.length - 1])}`;
}

function renderErrorState() {
    document.getElementById("total-transactions").textContent = "!";
    document.getElementById("signal-message").textContent = "Could not read the processed data file.";
    document.getElementById("category-list").innerHTML = '<p class="empty-state">Check that data/processed/dashboard.json exists.</p>';
    document.querySelector("#txn-table tbody").innerHTML = '<tr><td class="empty-state" colspan="4">Data unavailable. Refresh after rebuilding the ETL output.</td></tr>';
    document.getElementById("table-status").textContent = "Data unavailable";
}

function setLoadingState(isLoading) {
    document.getElementById("refresh-data").classList.toggle("is-loading", isLoading);
}

function getCategoryCounts(data) {
    const counts = data.reduce((result, txn) => {
        const category = String(txn.category || "other").toLowerCase();
        result[category] = (result[category] || 0) + 1;
        return result;
    }, {});
    return Object.entries(counts).map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
}

function amountOf(txn) {
    const amount = Number.parseFloat(String(txn.amount ?? 0).replace(/[^0-9.-]/g, ""));
    return Number.isFinite(amount) ? Math.abs(amount) : 0;
}

function isIncome(txn) {
    return INCOME_CATEGORIES.has(String(txn.category || "").toLowerCase());
}

function formatAmount(amount) {
    return new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 }).format(amount);
}

function formatDate(value) {
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? value || "Unknown date" : new Intl.DateTimeFormat("en", { month: "short", day: "2-digit", year: "numeric" }).format(date);
}

function capitalize(value) {
    return value.charAt(0).toUpperCase() + value.slice(1);
}

function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[character]));
}

document.addEventListener("DOMContentLoaded", loadDashboardData);
document.getElementById("refresh-data").addEventListener("click", loadDashboardData);
document.getElementById("transaction-search").addEventListener("input", event => renderTable(dashboardData, event.target.value));
