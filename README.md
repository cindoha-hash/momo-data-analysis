# MoMo SMS Data Processing & Analytics

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
