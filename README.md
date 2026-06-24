# Finance Bot

A local-first personal finance dashboard that automatically imports bank transaction CSV files, processes and categorizes spending, and visualizes financial data through an interactive web dashboard.

The system is fully offline, lightweight, and runs entirely on a local machine using Python, SQLite, and Streamlit.

---

## Features

* Local CSV-based transaction ingestion
* Automatic file detection and processing
* Rule-based transaction categorization
* SQLite-based persistent storage
* Interactive financial dashboard
* Filtering by category and transaction type
* Spending analytics with visual charts
* Fully offline and self-contained

---

## Project Structure

```
finance-bot/
│
├── venv/                  # Virtual environment (not committed)
├── imports/               # Place bank CSV files here
├── data/
│   └── data.db            # SQLite database
│
├── app.py                 # Streamlit dashboard
├── watcher.py             # CSV file watcher (auto ingestion)
├── parser.py             # CSV parsing and normalization
├── rules.py              # Categorization logic
├── db.py                 # Database operations
└── run.sh                # Optional startup script
```

---

## Requirements

* Python 3.10 or higher
* pip (Python package manager)
* Linux (tested on Ubuntu)

No external services or APIs are required.

---

## Installation

### 1. Clone or create project directory

```bash
mkdir finance-bot
cd finance-bot
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create required directories

```bash
mkdir imports data
```

---

## Usage

### Start the file watcher

The watcher monitors the `imports/` directory and automatically processes new CSV files.

```bash
source venv/bin/activate
python watcher.py
```

---

### Start the dashboard

In a separate terminal:

```bash
source venv/bin/activate
streamlit run app.py
```

---

### Add transaction data

1. Export a CSV file from your bank account
2. Place the file into:

```
imports/
```

The system will automatically:

* Detect the file
* Parse transactions
* Categorize spending
* Store data in the database

---

## Dashboard

Once running, open:

```
http://localhost:8501
```

The dashboard includes:

* Total spending overview
* Income vs expenses breakdown
* Category-based spending analysis
* Full transaction table
* Filtering by category and type

---

## Data Format

The system supports common bank CSV formats such as:

```
Transaction Date, Description, Amount
2026-01-01, Starbucks, -5.50
```

or:

```
Date, Post Date, Description, Amount
```

---

## Stopping the Application

Press `CTRL + C` in both terminals.

---

## Uninstallation

To remove the project completely:

```bash
rm -rf finance-bot
```

---

## Design Principles

* Fully local execution
* No external dependencies beyond Python packages
* Simple and transparent data processing
* Easily extensible architecture