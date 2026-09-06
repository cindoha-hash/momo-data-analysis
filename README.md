# MoMo SMS Data Processing & Analytics

## Team

**Team Name:** [TEAM_NAME]

## Team Members

| Name | Role |
|---|---|
| [Member 1] | Team Lead / Backend |
| [Member 2] | Data / ETL |
| [Member 3] | Database |
| [Member 4] | Frontend |
| [Member 5] | Documentation / QA |

## Project Description

This project processes MoMo SMS transaction data provided in XML format. The system will parse, clean, normalize, categorize, and store transaction data in a relational database. The processed data will then be used to generate analytical insights through a web-based dashboard.

### Planned Data Flow

MoMo XML → XML Parsing → Cleaning & Normalization → Categorization → SQLite Database → Analytics/API → Web Dashboard

## Project Objectives

- Process MoMo SMS data stored in XML format.
- Extract relevant transaction information.
- Clean and normalize transaction data.
- Categorize transactions according to their type.
- Store structured transaction data in a relational database.
- Generate useful transaction analytics.
- Present results through a simple and accessible dashboard.
- Practice collaborative software development using GitHub and Agile/Scrum.

## Planned Technology Stack

- **Backend/Data Processing:** Python, ElementTree/lxml, python-dateutil
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Optional API:** FastAPI, Pydantic
- **Collaboration:** GitHub, GitHub Projects
- **Architecture:** Draw.io

## Repository Structure

```text
.
├── README.md
├── .env.example
├── requirements.txt
├── index.html
├── docs/
│   ├── architecture.drawio
│   └── architecture.png
├── web/
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/
├── data/
│   ├── raw/
│   ├── processed/
│   └── logs/
│       └── dead_letter/
├── etl/
├── api/
├── scripts/
└── tests/
```

## System Architecture

The architecture diagram shows the major system components and their interactions, from raw MoMo XML input through processing and storage to analytics and the dashboard.

- **Architecture diagram:** `docs/architecture.png`
- **Editable Draw.io source:** `docs/architecture.drawio`
- **Draw.io link:** [PASTE YOUR DRAW.IO LINK HERE]

## Scrum Board

Our team uses a Scrum board to organize tasks and track project progress.

**Scrum Board:** [PASTE YOUR GITHUB PROJECTS / TRELLO / JIRA LINK HERE]

Required workflow:

- To Do
- In Progress
- Done

## Development Plan

### Phase 1 — Project Setup
- Create GitHub repository
- Add team members
- Define architecture
- Create Scrum board
- Define database schema

### Phase 2 — Data Processing
- Analyze XML structure
- Implement XML parser
- Clean and normalize transaction data
- Categorize transactions

### Phase 3 — Database
- Design relational schema
- Create SQLite database
- Load processed transactions
- Implement database queries

### Phase 4 — Analytics & API
- Generate transaction statistics
- Create analytics endpoints
- Prepare dashboard data

### Phase 5 — Frontend
- Build dashboard
- Display transaction statistics
- Add charts and tables
- Improve accessibility

### Phase 6 — Testing & Documentation
- Test XML parsing
- Test data cleaning
- Test categorization
- Test database operations
- Finalize documentation

## Team Workflow

The team will use GitHub for collaborative development. Each feature will be developed using a separate branch and merged into the main branch through pull requests.

Example:

```text
main
├── feature/xml-parser
├── feature/data-cleaning
├── feature/database
└── feature/dashboard
```

## Current Status

**Week 1 — Team Setup & Project Planning**

Current priorities:
- Repository setup
- Team collaboration
- Architecture
- Project organization
- Scrum planning

Implementation of the ETL pipeline, database, API, and dashboard will follow in subsequent development phases.
