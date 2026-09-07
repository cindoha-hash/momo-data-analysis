// Fetches processed data and renders it in the dashboard
// Full implementation to be completed in Phase 5 (Frontend)

async function loadDashboardData() {
    try {
        const response = await fetch("data/processed/dashboard.json");
        const data = await response.json();
        renderSummary(data);
        renderTable(data);
    } catch (err) {
        console.error("Could not load dashboard data:", err);
    }
}

function renderSummary(data) {
    document.getElementById("total-transactions").textContent = data.length || 0;
}

function renderTable(data) {
    const tbody = document.querySelector("#txn-table tbody");
    tbody.innerHTML = "";
    data.forEach(txn => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${txn.date}</td>
            <td>${txn.amount}</td>
            <td>${txn.category}</td>
        `;
        tbody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", loadDashboardData);
