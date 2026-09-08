import os

files = {}

files[".gitignore"] = """# Python
__pycache__/
*.pyc
.venv/
venv/

# Environment
.env

# Data
data/raw/*
!data/raw/.gitkeep
data/db.sqlite3
data/logs/*
!data/logs/.gitkeep
data/logs/dead_letter/*
!data/logs/dead_letter/.gitkeep

# OS
.DS_Store
"""

files[".env.example"] = """# Path to SQLite database file
DATABASE_URL=data/db.sqlite3

# Path to raw MoMo XML input
XML_INPUT_PATH=data/raw/momo.xml

# Path to processed dashboard JSON
DASHBOARD_JSON_PATH=data/processed/dashboard.json
"""

files["requirements.txt"] = """lxml==5.2.2
python-dateutil==2.9.0
fastapi==0.111.0
uvicorn==0.30.1
pydantic==2.7.4
"""

files["etl/__init__.py"] = "# ETL package for MoMo SMS data processing\n"

files["etl/config.py"] = """import os

# File paths
XML_INPUT_PATH = os.getenv("XML_INPUT_PATH", "data/raw/momo.xml")
DATABASE_PATH = os.getenv("DATABASE_URL", "data/db.sqlite3")
DASHBOARD_JSON_PATH = os.getenv("DASHBOARD_JSON_PATH", "data/processed/dashboard.json")
LOG_PATH = "data/logs/etl.log"
DEAD_LETTER_PATH = "data/logs/dead_letter/"

# Transaction categories (to be refined in Phase 2)
CATEGORIES = [
    "deposit",
    "withdrawal",
    "transfer",
    "payment",
    "airtime",
    "other",
]
"""

files["etl/parse_xml.py"] = '''"""
Parses raw MoMo SMS XML into a list of transaction dicts.
Implementation to be completed in Phase 2 (Data Processing).
"""
import xml.etree.ElementTree as ET
from etl.config import XML_INPUT_PATH


def parse_xml(file_path: str = XML_INPUT_PATH):
    """
    Parse the MoMo XML file and return a list of raw transaction records.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    transactions = []
    # TODO: loop through XML nodes and extract transaction fields
    # for sms in root.findall("sms"):
    #     transactions.append({...})

    return transactions


if __name__ == "__main__":
    data = parse_xml()
    print(f"Parsed {len(data)} transactions")
'''

files["etl/clean_normalize.py"] = '''"""
Cleans and normalizes raw transaction data:
amounts, dates, phone numbers.
Implementation to be completed in Phase 2.
"""
from dateutil import parser as date_parser


def normalize_amount(raw_amount: str) -> float:
    # TODO: strip currency symbols/commas, convert to float
    return float(raw_amount.replace(",", "").strip())


def normalize_date(raw_date: str):
    # TODO: handle multiple date formats from SMS text
    return date_parser.parse(raw_date)


def normalize_phone(raw_phone: str) -> str:
    # TODO: standardize phone number format
    return raw_phone.strip()


def clean_transactions(transactions: list) -> list:
    cleaned = []
    for txn in transactions:
        # TODO: apply normalization functions to each field
        cleaned.append(txn)
    return cleaned
'''

files["etl/categorize.py"] = '''"""
Applies simple rules to categorize each transaction.
Implementation to be completed in Phase 2.
"""
from etl.config import CATEGORIES


def categorize_transaction(txn: dict) -> str:
    """
    Given a cleaned transaction, return its category.
    """
    message = txn.get("message", "").lower()

    if "deposit" in message:
        return "deposit"
    elif "withdraw" in message:
        return "withdrawal"
    elif "transfer" in message:
        return "transfer"
    elif "payment" in message:
        return "payment"
    elif "airtime" in message:
        return "airtime"
    return "other"


def categorize_all(transactions: list) -> list:
    for txn in transactions:
        txn["category"] = categorize_transaction(txn)
    return transactions
'''

files["etl/load_db.py"] = '''"""
Creates tables and loads transactions into SQLite.
Implementation to be completed in Phase 3 (Database).
"""
import sqlite3
from etl.config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            date TEXT,
            phone TEXT,
            category TEXT,
            raw_message TEXT
        )
    """)
    conn.commit()
    conn.close()


def load_transactions(transactions: list):
    conn = get_connection()
    cursor = conn.cursor()
    for txn in transactions:
        cursor.execute(
            "INSERT INTO transactions (amount, date, phone, category, raw_message) VALUES (?, ?, ?, ?, ?)",
            (
                txn.get("amount"),
                txn.get("date"),
                txn.get("phone"),
                txn.get("category"),
                txn.get("message"),
            ),
        )
    conn.commit()
    conn.close()
'''

files["etl/run.py"] = '''"""
Main ETL pipeline: parse -> clean -> categorize -> load -> export JSON
"""
from etl.parse_xml import parse_xml
from etl.clean_normalize import clean_transactions
from etl.categorize import categorize_all
from etl.load_db import create_tables, load_transactions


def run():
    print("Step 1: Parsing XML...")
    raw_data = parse_xml()

    print("Step 2: Cleaning data...")
    cleaned_data = clean_transactions(raw_data)

    print("Step 3: Categorizing transactions...")
    categorized_data = categorize_all(cleaned_data)

    print("Step 4: Loading into database...")
    create_tables()
    load_transactions(categorized_data)

    print("ETL pipeline complete.")


if __name__ == "__main__":
    run()
'''

files["api/__init__.py"] = "# Optional FastAPI package for analytics endpoints\n"

files["api/db.py"] = """import sqlite3
from etl.config import DATABASE_PATH


def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
"""

files["api/schemas.py"] = """from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    amount: float
    date: str
    phone: str
    category: str
    raw_message: str
"""

files["api/app.py"] = '''"""
Minimal FastAPI app exposing /transactions and /analytics
Optional bonus - to be implemented in Phase 4.
"""
from fastapi import FastAPI
from api.db import get_connection

app = FastAPI(title="MoMo SMS Analytics API")


@app.get("/")
def root():
    return {"message": "MoMo SMS Analytics API is running"}


@app.get("/transactions")
def get_transactions():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM transactions").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/analytics")
def get_analytics():
    conn = get_connection()
    total = conn.execute("SELECT COUNT(*) as count FROM transactions").fetchone()
    conn.close()
    return {"total_transactions": total["count"] if total else 0}
'''

files["scripts/run_etl.sh"] = """#!/bin/bash
python etl/run.py --xml data/raw/momo.xml
"""

files["scripts/export_json.sh"] = """#!/bin/bash
python -c \"
from etl.load_db import get_connection
import json
from etl.config import DASHBOARD_JSON_PATH

conn = get_connection()
conn.row_factory = None
rows = conn.execute('SELECT * FROM transactions').fetchall()
conn.close()

with open(DASHBOARD_JSON_PATH, 'w') as f:
    json.dump(rows, f, indent=2)

print('Exported dashboard.json')
\"
"""

files["scripts/serve_frontend.sh"] = """#!/bin/bash
python -m http.server 8000
"""

files["tests/test_parse_xml.py"] = '''import unittest
from etl.parse_xml import parse_xml


class TestParseXML(unittest.TestCase):
    def test_returns_list(self):
        # TODO: point to a small sample XML file for testing
        result = []
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
'''

files["tests/test_clean_normalize.py"] = '''import unittest
from etl.clean_normalize import normalize_amount, normalize_phone


class TestCleanNormalize(unittest.TestCase):
    def test_normalize_amount(self):
        self.assertEqual(normalize_amount("1,000"), 1000.0)

    def test_normalize_phone(self):
        self.assertEqual(normalize_phone(" 0788123456 "), "0788123456")


if __name__ == "__main__":
    unittest.main()
'''

files["tests/test_categorize.py"] = '''import unittest
from etl.categorize import categorize_transaction


class TestCategorize(unittest.TestCase):
    def test_deposit(self):
        txn = {"message": "You have received a deposit of 1000 RWF"}
        self.assertEqual(categorize_transaction(txn), "deposit")

    def test_unknown(self):
        txn = {"message": "Some random message"}
        self.assertEqual(categorize_transaction(txn), "other")


if __name__ == "__main__":
    unittest.main()
'''

files["index.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MoMo SMS Analytics Dashboard</title>
    <link rel="stylesheet" href="web/styles.css">
</head>
<body>
    <header>
        <h1>MoMo SMS Analytics Dashboard</h1>
    </header>

    <main>
        <section id="summary">
            <h2>Summary</h2>
            <p>Total Transactions: <span id="total-transactions">--</span></p>
        </section>

        <section id="charts">
            <h2>Transaction Breakdown</h2>
            <canvas id="category-chart"></canvas>
        </section>

        <section id="transactions-table">
            <h2>Recent Transactions</h2>
            <table id="txn-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Category</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </section>
    </main>

    <script src="web/chart_handler.js"></script>
</body>
</html>
"""

files["web/styles.css"] = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
    color: #222;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem 2rem;
}

main {
    padding: 2rem;
}

section {
    background: white;
    margin-bottom: 1.5rem;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    text-align: left;
    padding: 0.5rem;
    border-bottom: 1px solid #ddd;
}
"""

files["web/chart_handler.js"] = """// Fetches processed data and renders it in the dashboard
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
"""

files["README.md"] = """# MoMo SMS Data Processing & Analytics

## Team

**Team Name:** MoMo Analytics Team

### Team Members

| Name | Role |
|------|------|
| IRADUKUNDA CYUSA Kevin | Backend / ETL / Architecture / Scrum Board |
| [Fill Name] | Frontend / Documentation |

## Repository

GitHub Repo: https://github.com/cindoha-hash/momo-data-analysis

## Project Description

This project processes MoMo SMS transaction data provided in XML format. We parse the raw XML, clean and normalize the data (fixing dates, amounts, phone numbers), sort transactions into categories (like deposits, withdrawals, transfers, etc.), and store everything in a SQLite database. From there we build a simple web dashboard so we can see stats like total transactions, most common category, and spending trends over time.

## Planned Data Flow

MoMo XML -> XML Parsing -> Cleaning & Normalization -> Categorization -> SQLite Database -> Analytics/API -> Web Dashboard

## Project Objectives

- Process MoMo SMS data stored in XML format
- Extract relevant transaction information
- Clean and normalize transaction data
- Categorize transactions according to their type
- Store structured transaction data in a relational database
- Generate useful transaction analytics
- Present results through a simple and accessible dashboard
- Practice collaborative software development using GitHub and Agile/Scrum

## Planned Technology Stack

- **Backend/Data Processing:** Python, ElementTree/lxml, python-dateutil
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Optional API:** FastAPI, Pydantic
- **Collaboration:** GitHub, GitHub Projects
- **Architecture:** Draw.io

## Repository Structure

```
.
|-- README.md
|-- .env.example
|-- requirements.txt
|-- index.html
|-- docs/
|   |-- architecture.drawio
|   |-- architecture.png
|-- web/
|   |-- styles.css
|   |-- chart_handler.js
|   |-- assets/
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- logs/
|       |-- dead_letter/
|-- etl/
|-- api/
|-- scripts/
|-- tests/
```

## System Architecture

The architecture diagram shows how data moves through the system, from the raw MoMo XML file, through parsing and cleaning, into the database, and finally out to the dashboard.

- Architecture diagram: `docs/architecture.png`
- Editable Draw.io source: `docs/architecture.drawio`
- Draw.io link: [Paste your Draw.io share link here]

## Scrum Board

We're using a Scrum board to keep track of tasks and progress.

**Scrum Board:** [Paste your GitHub Projects link here]

Columns: To Do -> In Progress -> Done

## Development Plan

**Phase 1 - Project Setup**
- Create GitHub repository
- Add team members
- Define architecture
- Create Scrum board
- Define database schema

**Phase 2 - Data Processing**
- Analyze XML structure
- Implement XML parser
- Clean and normalize transaction data
- Categorize transactions

**Phase 3 - Database**
- Design relational schema
- Create SQLite database
- Load processed transactions
- Implement database queries

**Phase 4 - Analytics & API**
- Generate transaction statistics
- Create analytics endpoints
- Prepare dashboard data

**Phase 5 - Frontend**
- Build dashboard
- Display transaction statistics
- Add charts and tables
- Improve accessibility

**Phase 6 - Testing & Documentation**
- Test XML parsing
- Test data cleaning
- Test categorization
- Test database operations
- Finalize documentation

## Team Workflow

We're using GitHub for collaborative development. Each feature is built on its own branch and merged into main through pull requests.

```
main
|-- feature/xml-parser
|-- feature/data-cleaning
|-- feature/database
|-- feature/dashboard
```

## Current Status

**Week 1 - Team Setup & Project Planning**

Current priorities:
- Repository setup
- Team collaboration
- Architecture
- Project organization
- Scrum planning

Implementation of the ETL pipeline, database, API, and dashboard will follow in the next phases.

## Hosting

The frontend dashboard is hosted on GitHub Pages: https://cindoha-hash.github.io/momo-data-analysis/
"""

# Placeholder files so empty folders get tracked by git
placeholders = [
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/logs/.gitkeep",
    "data/logs/dead_letter/.gitkeep",
]
for p in placeholders:
    files[p] = ""

# Write everything
for path, content in files.items():
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", newline="\n") as f:
        f.write(content)
    print(f"Wrote {path}")

print("\\nAll files created successfully.")
