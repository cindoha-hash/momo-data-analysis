# MoMo SMS Data Processing & Analytics

## Team

**Team Name:** MoMo Analytics Team

### Team Members

| Name | Role |
|------|------|
| IRADUKUNDA Cyusa Kevin | Backend / ETL / Database / API |
| Emmanuel Chetachi Amarikwa | Frontend / Dashboard / Documentation g / Design document  |
| Sylvie Uwera | SQL queries / Database testing / Query validation |

## Repository

GitHub Repo: https://github.com/cindoha-hash/momo-data-analysis.git

## Project Description

This project turns MoMo SMS records from XML into structured transaction data. The ETL pipeline parses each record, normalizes dates, amounts, and phone numbers, assigns a category, and prepares the results for database queries and the dashboard. The database work covers customers, transaction parties, categories, transaction records, and processing logs.

## Data Flow

MoMo XML -> XML Parsing -> Cleaning & Normalization -> Categorization -> SQLite Database -> Analytics/API -> Web Dashboard

## Project Objectives

- Process MoMo SMS data stored in XML format
- Extract relevant transaction information
- Clean and normalize transaction data
- Categorize transactions according to their type
- Store structured transaction data in a relational database
- Generate useful transaction analytics
- Present results through a simple and accessible dashboard
- Track the team's work through GitHub branches, commits, pull requests, and Scrum tasks

## Technology Stack

- **Backend/Data Processing:** Python, ElementTree/lxml, python-dateutil
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Optional API:** FastAPI, Pydantic
- **Collaboration:** GitHub, GitHub Projects
- **Architecture:** Draw.io

## Repository Structure

.
|-- README.md
|-- .env.example
|-- requirements.txt
|-- index.html
|-- docs/
| |-- architecture.drawio
| |-- architecture.png
| |-- erd_diagram.png
|-- database/
| |-- database_setup.sql
| |-- sample_queries.sql
| |-- security_rules.sql
|-- examples/
| |-- json_schemas.json
|-- web/
| |-- styles.css
| |-- chart_handler.js
| |-- assets/
|-- data/
| |-- raw/
| |-- processed/
| |-- logs/
| |-- dead_letter/
|-- etl/
|-- api/
|-- scripts/
|-- tests/


## System Architecture

The architecture diagram shows how data moves through the system, from the raw MoMo XML file, through parsing and cleaning, into the database, and finally out to the dashboard.

- Architecture diagram: `docs/architecture.png`
- Editable Draw.io source: `docs/architecture.drawio`
- Week 2 ERD: `docs/erd_diagram.png`

## Week 2 Database Deliverables

- Database schema, constraints, indexes, and sample data: `database/database_setup.sql`
- Sample joins, filters, and aggregate queries: `database/sample_queries.sql`
- Security and accuracy rules: `database/security_rules.sql`
- JSON entity models and SQL-to-JSON mapping: `examples/json_schemas.json`

## Scrum Board

We're using a Scrum board to keep track of tasks and progress.

**Trello Board:** https://trello.com/b/aadeNi62/momo-analytics-project-board

Columns: To Do -> In Progress -> Done

Local task board: [docs/scrum-board.md](docs/scrum-board.md)

## Assignment Requirements and Expectations

This project is being developed for the **Team Setup and Project Planning** assessment. The team is building a small full-stack application that processes MoMo SMS data and presents useful transaction analytics.

### Required Project Work

- Create and maintain a shared GitHub repository.
- Add all teammates as repository collaborators.
- Keep this README updated with the team name, member list, project description, setup instructions, and project links.
- Organize the repository into data, ETL, API, frontend, scripts, documentation, and tests.
- Design a high-level architecture showing the flow from MoMo XML input through processing, storage, API or analytics, and the dashboard.
- Create a Scrum board with **To Do**, **In Progress**, and **Done** columns.
- Add at least three initial tasks to the Scrum board and update task status as work progresses.

### Expected System Capabilities

- Parse MoMo SMS records from XML.
- Clean and normalize transaction amounts, dates, and phone numbers.
- Categorize transactions such as deposits, withdrawals, transfers, payments, and airtime.
- Store structured transactions in a relational database, using SQLite for this project.
- Produce processed data and analytics for the frontend dashboard.
- Provide a usable web interface with summary statistics, charts, and transaction tables.
- Include tests for parsing, cleaning, and categorization.

### Assessment Deliverables

- GitHub repository link: https://github.com/cindoha-hash/momo-data-analysis.git
- Architecture diagram: [docs/architecture.png](docs/architecture.png)
- Editable architecture source: [docs/architecture.drawio](docs/architecture.drawio)
- ERD diagram: [docs/erd_diagram.png](docs/erd_diagram.png)
- Database setup script: [database/database_setup.sql](database/database_setup.sql)
- Sample queries: [database/sample_queries.sql](database/sample_queries.sql)
- Security rules: [database/security_rules.sql](database/security_rules.sql)
- JSON models: [examples/json_schemas.json](examples/json_schemas.json)
- Scrum board: [docs/scrum-board.md](docs/scrum-board.md)
- External Scrum board URL: https://trello.com/b/aadeNi62/momo-analytics-project-board

### Completion Checklist

- [x] Repository created and README added.
- [ ] All teammates invited as GitHub collaborators.
- [x] Architecture diagram committed to the repository.
- [x] Scrum board structure and initial tasks documented.
- [x] External Scrum board URL added above.
- [ ] Final dashboard and data-processing workflow demonstrated with sample XML data.

## Development Roadmap

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

main
|-- feature/xml-parser
|-- feature/data-cleaning
|-- feature/database
|-- feature/dashboard


## Current Status

**Week 2 - Database Design and Implementation**

Current focus:
- Database schema and ERD
- Sample SQL queries and security rules
- JSON modeling and SQL-to-JSON mapping
- MySQL testing evidence and design documentation

The dashboard is available locally, and the ETL, database, API, and deployment workflow are being completed in parallel.

## Hosting

The website will be deployed on  github page .
https://cindoha-hash.github.io/momo-data-analysis/


