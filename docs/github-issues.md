# ⚡ StackFlow — GitHub Issues Tracker

**Personal Finance + Crypto Intelligence Platform**
35 tickets · ~70 hours · 7 weeks · Due April 29th

-----

## 🛠 Epic 1: Project Setup

-----

### SF-001 — Initialize GitHub repository and folder structure

**Priority:** High | **Effort:** 1h | **Week:** 1
**Labels:** `setup` `github`

Create the GitHub repo and base folder structure for the entire StackFlow project.

**Acceptance Criteria:**

- [ ] Repo named `stackflow` created and pushed to GitHub
- [ ] Folders created: `producers/`, `consumers/`, `spark_jobs/`, `dbt/`, `airflow/dags/`, `sql/`, `streamlit/`, `models/`
- [ ] `.gitignore` added (Python, env files, `__pycache__`, `.env`)
- [ ] `README.md` with project title and placeholder sections
- [ ] `.env.example` file created listing all required environment variables

-----

### SF-002 — Set up local Python environment and dependencies

**Priority:** High | **Effort:** 1h | **Week:** 1
**Labels:** `setup` `python`

Create a virtual environment and install all required Python packages.

**Acceptance Criteria:**

- [ ] `requirements.txt` created with all dependencies
- [ ] Virtual environment created and activated
- [ ] Packages installed: `sqlalchemy`, `psycopg2-binary`, `kafka-python`, `faker`, `openai`, `streamlit`, `pyspark`, `python-dotenv`, `requests`, `plotly`, `pandas`
- [ ] `pip freeze` output verified

-----

### SF-003 — Set up Docker Compose for local services

**Priority:** High | **Effort:** 2h | **Week:** 1
**Labels:** `setup` `docker` `kafka`

Configure Docker Compose to run Kafka, Zookeeper, and PostgreSQL locally.

**Acceptance Criteria:**

- [ ] `docker-compose.yml` created
- [ ] Kafka + Zookeeper running on port 9092
- [ ] PostgreSQL running on port 5432
- [ ] Airflow running on port 8080
- [ ] All containers start cleanly with `docker-compose up`
- [ ] Services verified healthy via `docker ps`

-----

### SF-004 — Set up AWS account and core services

**Priority:** High | **Effort:** 3h | **Week:** 1
**Labels:** `setup` `aws`

Configure AWS S3 bucket, Redshift cluster, and IAM roles.

**Acceptance Criteria:**

- [ ] S3 bucket `stackflow-data-lake` created with `raw/`, `processed/`, `curated/` prefixes
- [ ] Redshift cluster provisioned (dc2.large, paused when not in use)
- [ ] IAM role created allowing Redshift to read from S3
- [ ] AWS credentials configured in `.env` file
- [ ] Boto3 test connection verified with a sample `put_object` call

-----

### SF-005 — Set up Databricks Community Edition

**Priority:** High | **Effort:** 2h | **Week:** 1
**Labels:** `setup` `databricks`

Create a free Databricks account and connect it to S3.

**Acceptance Criteria:**

- [ ] Databricks Community Edition account created at community.cloud.databricks.com
- [ ] Cluster created (single node, 15.4 LTS runtime)
- [ ] AWS S3 credentials mounted in Databricks via DBFS
- [ ] Test notebook reads a sample file from S3 successfully
- [ ] Databricks personal access token saved to `.env`

-----

## 🏗 Epic 2: OOP & Database Layer

-----

### SF-006 — Design and implement Transaction OOP class with CRUD

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy`

Build the Transaction class using SQLAlchemy ORM mapping to the transactions table.

**Acceptance Criteria:**

- [ ] Transaction class defined with fields: id, amount, category, description, date, type (income/expense), source
- [ ] `transactions` table auto-created via SQLAlchemy
- [ ] `add_transaction()` method works
- [ ] `get_transaction(id)` method works
- [ ] `update_transaction()` method works
- [ ] `delete_transaction()` method works
- [ ] All 4 CRUD operations tested manually

-----

### SF-007 — Design and implement SavingsGoal OOP class with CRUD

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy`

Build the SavingsGoal class tracking progress toward the house down payment.

**Acceptance Criteria:**

- [ ] SavingsGoal class with fields: id, name, target_amount, current_amount, deadline, monthly_contribution, status
- [ ] `savings_goals` table auto-created
- [ ] Full CRUD methods implemented and tested
- [ ] `calculate_trajectory()` method returns months_remaining and on_track boolean
- [ ] `model_scenario(extra_monthly)` method returns new projected completion date

-----

### SF-008 — Design and implement Investment OOP class with CRUD

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy`

Track investment contributions and holdings across accounts.

**Acceptance Criteria:**

- [ ] Investment class with fields: id, account_type (401k/Roth IRA/brokerage), ticker, shares, avg_cost_basis, date_added
- [ ] `investments` table auto-created
- [ ] Full CRUD methods implemented and tested
- [ ] `get_current_value()` method fetches live price and calculates total value

-----

### SF-009 — Design and implement Debt OOP class with CRUD

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy`

Track all debts and model payoff strategies.

**Acceptance Criteria:**

- [ ] Debt class with fields: id, name, balance, interest_rate, minimum_payment, debt_type (student_loan/credit_card/other)
- [ ] `debts` table auto-created
- [ ] Full CRUD methods implemented and tested
- [ ] `avalanche_payoff()` method returns payoff schedule sorted by highest interest rate first
- [ ] `snowball_payoff()` method returns payoff schedule sorted by lowest balance first

-----

### SF-010 — Design and implement TaxRecord OOP class with CRUD

**Priority:** Medium | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy`

Track income and estimate quarterly tax liability.

**Acceptance Criteria:**

- [ ] TaxRecord class with fields: id, year, quarter, gross_income, estimated_tax_owed, tax_paid, deductions
- [ ] `tax_records` table auto-created
- [ ] Full CRUD methods implemented and tested
- [ ] `estimate_quarterly_tax()` method calculates owed amount based on income and filing status
- [ ] `calculate_effective_rate()` method returns effective tax rate

-----

### SF-011 — Design and implement CryptoHolding OOP class with CRUD

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `oop` `database` `sqlalchemy` `crypto`

Track crypto holdings and link to live price data.

**Acceptance Criteria:**

- [ ] CryptoHolding class with fields: id, symbol, quantity, avg_purchase_price, purchase_date, exchange
- [ ] `crypto_holdings` table auto-created
- [ ] Full CRUD methods implemented and tested
- [ ] `get_current_pnl()` method fetches live price and returns unrealized P&L
- [ ] `get_portfolio_value()` class method returns total value of all holdings

-----

### SF-012 — Seed database with AI-generated sample data

**Priority:** High | **Effort:** 2h | **Week:** 2
**Labels:** `ai` `database` `seeding`

Use OpenAI API to generate realistic sample financial records inserted via OOP classes.

**Acceptance Criteria:**

- [ ] OpenAI API connected and working
- [ ] GPT generates 6 months of realistic transactions across all categories
- [ ] GPT generates 2 savings goals, 3 debts, 4 investments, 2 tax records
- [ ] All records inserted using OOP CRUD methods (not raw SQL)
- [ ] Data is realistic (believable amounts, proper categories, real ticker symbols)
- [ ] Seed script is idempotent — running it twice doesn’t duplicate records

-----

## ⚡ Epic 3: Live Crypto Streaming Pipeline

-----

### SF-013 — Connect to Coinbase Advanced Trade API

**Priority:** High | **Effort:** 3h | **Week:** 3
**Labels:** `crypto` `api` `python`

Set up authenticated connection to Coinbase API and verify live price data is accessible.

**Acceptance Criteria:**

- [ ] Coinbase API credentials created and stored in `.env`
- [ ] Python client connects and fetches current BTC, ETH, SOL prices
- [ ] Rate limit handling implemented (429 errors caught and retried with backoff)
- [ ] API downtime handling — connection errors caught and logged without crashing
- [ ] Test script prints live prices successfully

-----

### SF-014 — Build Kafka producer for live crypto price events

**Priority:** High | **Effort:** 3h | **Week:** 3
**Labels:** `kafka` `streaming` `crypto`

Producer polls Coinbase every 10 seconds and publishes price tick events to Kafka.

**Acceptance Criteria:**

- [ ] `crypto_prices` Kafka topic created
- [ ] Producer polls Coinbase API every 10 seconds for BTC, ETH, SOL, DOGE prices
- [ ] Event payload includes: symbol, price, volume_24h, percent_change_24h, timestamp, exchange
- [ ] Producer handles API downtime gracefully — logs error and retries after 30 seconds
- [ ] Producer handles rate limiting with exponential backoff
- [ ] Events verified in Kafka consumer logs

-----

### SF-015 — Build Kafka producer for portfolio value events

**Priority:** Medium | **Effort:** 2h | **Week:** 3
**Labels:** `kafka` `streaming` `crypto`

Producer calculates and publishes your total portfolio value every minute using live prices.

**Acceptance Criteria:**

- [ ] `portfolio_snapshots` Kafka topic created
- [ ] Producer reads current holdings from PostgreSQL every 60 seconds
- [ ] Calculates total portfolio value using live Coinbase prices
- [ ] Publishes snapshot: total_value, pnl_today, pnl_percent, timestamp
- [ ] Verified producing events consistently

-----

### SF-016 — Build Kafka consumer that writes raw events to S3

**Priority:** High | **Effort:** 3h | **Week:** 3
**Labels:** `kafka` `s3` `aws` `streaming`

Consumer reads from Kafka topics and lands raw events in S3 data lake partitioned by date.

**Acceptance Criteria:**

- [ ] Consumer reads from `crypto_prices` and `portfolio_snapshots` topics
- [ ] Buffers 50 records then flushes to S3 as JSON
- [ ] S3 key structure: `raw/{topic}/year=YYYY/month=MM/day=DD/{timestamp}.json`
- [ ] Consumer recovers gracefully from Kafka connection drops
- [ ] Consumer recovers gracefully from S3 write failures
- [ ] Dead letter queue logs any records that fail to write after 3 retries

-----

### SF-017 — Build pipeline incident simulator

**Priority:** Medium | **Effort:** 2h | **Week:** 3
**Labels:** `streaming` `testing` `python`

Script that intentionally injects realistic pipeline failures to practice incident response.

**Acceptance Criteria:**

- [ ] `simulate_incident.py` script with selectable failure modes
- [ ] Mode 1: API downtime (blocks Coinbase calls for N minutes)
- [ ] Mode 2: Schema change (renames `price` field to `last_price`)
- [ ] Mode 3: Corrupt data (injects null prices and negative volumes)
- [ ] Mode 4: Late arriving data (sends events with timestamps 3 hours in the past)
- [ ] Each mode logs what it’s doing so you can practice diagnosing it
- [ ] `RUNBOOK.md` created documenting how to detect and fix each incident type

-----

## ⚙️ Epic 4: Databricks + Spark Processing

-----

### SF-018 — Build Databricks notebook to process raw crypto price data

**Priority:** High | **Effort:** 4h | **Week:** 4
**Labels:** `databricks` `spark` `delta-lake`

Spark job reads raw S3 JSON, cleans it, enriches it, and writes Delta tables.

**Acceptance Criteria:**

- [ ] Notebook reads from `s3://stackflow-data-lake/raw/crypto_prices/`
- [ ] Drops duplicate events on (symbol, timestamp)
- [ ] Filters records where price <= 0 or price is null
- [ ] Adds `price_change_1h` and `price_change_24h` calculated columns
- [ ] Adds `is_volatile` flag (True if 24h change > 10%)
- [ ] Writes to Delta table: `stackflow.silver.crypto_prices`
- [ ] Delta table has Z-ORDER optimization on symbol and timestamp

-----

### SF-019 — Build Databricks notebook to process portfolio snapshots

**Priority:** High | **Effort:** 3h | **Week:** 4
**Labels:** `databricks` `spark` `delta-lake`

Processes raw portfolio snapshot events into a clean Delta table.

**Acceptance Criteria:**

- [ ] Reads from `s3://stackflow-data-lake/raw/portfolio_snapshots/`
- [ ] Deduplicates on timestamp
- [ ] Calculates `rolling_7d_avg_value` using Spark window functions
- [ ] Flags days where portfolio dropped more than 5% as `high_loss_day = true`
- [ ] Writes to Delta table: `stackflow.silver.portfolio_snapshots`

-----

### SF-020 — Implement Delta Lake time travel on crypto prices

**Priority:** Medium | **Effort:** 2h | **Week:** 4
**Labels:** `databricks` `delta-lake`

Demonstrate Delta Lake’s time travel capability to query historical versions of your data.

**Acceptance Criteria:**

- [ ] Delta table has at least 3 versions committed
- [ ] Notebook demonstrates querying table AS OF a specific timestamp
- [ ] Notebook demonstrates querying table AS OF a specific version number
- [ ] Use case documented: recovering from a bad Spark job that corrupted prices
- [ ] `DESCRIBE HISTORY` output saved as a screenshot in the repo

-----

### SF-021 — Set up Databricks Unity Catalog for data governance

**Priority:** Medium | **Effort:** 2h | **Week:** 4
**Labels:** `databricks` `unity-catalog` `governance`

Register all Delta tables in Unity Catalog with proper documentation.

**Acceptance Criteria:**

- [ ] `stackflow` catalog created in Unity Catalog
- [ ] `bronze`, `silver`, `gold` schemas created
- [ ] All Delta tables registered with descriptions
- [ ] Column-level comments added to all key fields
- [ ] Data lineage visible in Unity Catalog UI
- [ ] Screenshot of lineage graph saved in repo

-----

## 🏛 Epic 5: Data Warehouse

-----

### SF-022 — Create Redshift staging and warehouse schema

**Priority:** High | **Effort:** 2h | **Week:** 5
**Labels:** `redshift` `sql` `warehouse`

Define staging and warehouse tables in Redshift using star schema design.

**Acceptance Criteria:**

- [ ] `staging` schema with: `stg_crypto_prices`, `stg_portfolio_snapshots`, `stg_transactions`
- [ ] `warehouse` schema with: `dim_crypto_assets`, `dim_accounts`, `fact_price_ticks`, `fact_portfolio_daily`, `fact_transactions`
- [ ] All foreign keys and data types correctly defined
- [ ] SQL script committed to `sql/create_tables.sql`

-----

### SF-023 — Implement Redshift COPY to load from S3 Delta files

**Priority:** High | **Effort:** 2h | **Week:** 5
**Labels:** `redshift` `s3` `aws` `sql`

Load processed Parquet/Delta files from S3 into Redshift staging tables.

**Acceptance Criteria:**

- [ ] COPY command loads crypto prices into `stg_crypto_prices`
- [ ] COPY command loads portfolio snapshots into `stg_portfolio_snapshots`
- [ ] IAM role permissions verified
- [ ] Load tested with at least 5,000 rows
- [ ] Python function wrapping all COPY commands committed to codebase
- [ ] Incremental load logic implemented (only loads new partitions)

-----

## 🔧 Epic 6: dbt Modeling

-----

### SF-024 — Set up dbt project and Redshift connection

**Priority:** High | **Effort:** 1.5h | **Week:** 5
**Labels:** `dbt` `redshift`

Initialize dbt project and verify Redshift connection.

**Acceptance Criteria:**

- [ ] dbt project initialized in `dbt/` folder
- [ ] `profiles.yml` configured for Redshift (credentials in `.env`, not hardcoded)
- [ ] `dbt debug` passes with no errors
- [ ] dbt project committed to GitHub (no credentials)

-----

### SF-025 — Build dbt staging models

**Priority:** High | **Effort:** 2h | **Week:** 5
**Labels:** `dbt` `sql`

Light cleanup staging models — one per source table.

**Acceptance Criteria:**

- [ ] `stg_crypto_prices.sql` created
- [ ] `stg_portfolio_snapshots.sql` created
- [ ] `stg_transactions.sql` created
- [ ] All staging models materialize as views
- [ ] `dbt run --select staging` succeeds cleanly

-----

### SF-026 — Build dbt mart models for analytics

**Priority:** High | **Effort:** 3h | **Week:** 5
**Labels:** `dbt` `sql` `analytics`

Final analytics-ready mart models used by the Streamlit dashboard.

**Acceptance Criteria:**

- [ ] `mart_crypto_daily_summary.sql` — daily OHLC-style summary per coin
- [ ] `mart_portfolio_growth.sql` — portfolio value over time with 7d/30d rolling averages
- [ ] `mart_savings_trajectory.sql` — monthly savings vs house goal target
- [ ] `mart_debt_payoff_schedule.sql` — avalanche vs snowball comparison by month
- [ ] `mart_monthly_spending.sql` — spending by category per month
- [ ] All marts materialize as tables
- [ ] `dbt run` succeeds for all models

-----

### SF-027 — Add dbt tests and documentation

**Priority:** Medium | **Effort:** 1.5h | **Week:** 5
**Labels:** `dbt` `data-quality`

Data quality tests and model documentation across all dbt models.

**Acceptance Criteria:**

- [ ] `unique` and `not_null` tests on all primary keys
- [ ] `accepted_values` test on transaction type (income/expense)
- [ ] `accepted_range` test on price columns (> 0)
- [ ] `dbt test` passes with 0 failures
- [ ] All models documented in `schema.yml` with column descriptions

-----

## 🔄 Epic 7: Orchestration

-----

### SF-028 — Build daily finance pipeline Airflow DAG

**Priority:** High | **Effort:** 3h | **Week:** 5
**Labels:** `airflow` `orchestration`

DAG orchestrating the full daily pipeline end-to-end.

**Acceptance Criteria:**

- [ ] DAG named `stackflow_daily_pipeline`
- [ ] Scheduled `@daily` at 6am
- [ ] Task order: trigger_databricks_job → load_to_redshift → run_dbt → test_dbt → notify
- [ ] Each task has `retries=3` and `retry_delay=10min`
- [ ] Slack or email alert on failure
- [ ] DAG runs end-to-end successfully at least once

-----

### SF-029 — Build streaming health monitor Airflow DAG

**Priority:** Medium | **Effort:** 2h | **Week:** 5
**Labels:** `airflow` `orchestration` `monitoring`

DAG that monitors the health of your Kafka producers and alerts if data stops flowing.

**Acceptance Criteria:**

- [ ] DAG named `stackflow_stream_monitor` runs every 30 minutes
- [ ] Checks S3 for new files in the last 30 minutes
- [ ] If no new files found, triggers an alert: “Kafka producer may be down”
- [ ] Checks that latest crypto price timestamp is not more than 15 minutes old
- [ ] Alert includes which topic stopped and the last successful timestamp

-----

## 🖥 Epic 8: Streamlit Dashboard

-----

### SF-030 — Build Streamlit app shell and navigation

**Priority:** High | **Effort:** 2h | **Week:** 6
**Labels:** `streamlit` `frontend`

Base Streamlit app with navigation and database connection.

**Acceptance Criteria:**

- [ ] App runs with `streamlit run app.py`
- [ ] Sidebar navigation: Overview, Crypto, Savings Goal, Debt Tracker, Tax Estimator, AI Assistant
- [ ] Database connection via SQLAlchemy using `.env` credentials
- [ ] App loads without errors
- [ ] Basic NestIQ-style header with StackFlow branding

-----

### SF-031 — Build Overview and Crypto dashboard pages

**Priority:** High | **Effort:** 3h | **Week:** 6
**Labels:** `streamlit` `frontend` `crypto`

Main dashboard showing net worth, crypto portfolio, and live price feed.

**Acceptance Criteria:**

- [ ] Overview page: net worth KPI card, monthly savings rate, debt-to-income ratio, days until house goal
- [ ] Crypto page: live price table (auto-refreshes every 30s), portfolio value chart over time, P&L per coin, volatility flags
- [ ] All crypto data pulls from Redshift mart tables
- [ ] Live price widget calls Coinbase API directly for real-time display

-----

### SF-032 — Build Savings Goal and Debt Tracker pages

**Priority:** High | **Effort:** 2h | **Week:** 6
**Labels:** `streamlit` `frontend`

Savings trajectory and debt payoff pages.

**Acceptance Criteria:**

- [ ] Savings page: progress bar to house goal, trajectory line chart (actual vs target), scenario slider (“what if I save $X more/month?”)
- [ ] Debt page: total debt KPI, avalanche vs snowball comparison chart, months to debt-free under each strategy
- [ ] Both pages use SQLAlchemy OOP classes to read from PostgreSQL

-----

## 🤖 Epic 9: AI Integration

-----

### SF-033 — Build AI natural language financial query engine

**Priority:** High | **Effort:** 3h | **Week:** 6
**Labels:** `ai` `openai` `sql`

User types a plain English question about their finances, AI returns an answer.

**Acceptance Criteria:**

- [ ] OpenAI API connected
- [ ] System prompt includes full database schema and current financial context
- [ ] Flow: question → GPT generates SQL → runs on Redshift → result back to GPT → plain English answer
- [ ] Tested with 10 real questions (spending, savings, crypto, debt)
- [ ] Handles invalid queries without crashing
- [ ] Integrated into AI Assistant page in Streamlit

-----

### SF-034 — Build AI monthly financial health summary

**Priority:** Medium | **Effort:** 2h | **Week:** 6
**Labels:** `ai` `openai`

AI generates a personalized monthly financial summary and action items.

**Acceptance Criteria:**

- [ ] Runs on the 1st of each month via Airflow DAG task
- [ ] Pulls last month’s spending, savings rate, crypto P&L, debt payments from Redshift
- [ ] GPT generates a 3-paragraph summary: what went well, what didn’t, 3 specific action items
- [ ] Summary stored in database and displayed in Streamlit Overview page
- [ ] Tested for at least 2 simulated months of data

-----

## ✅ Epic 10: Polish & Delivery

-----

### SF-035 — End-to-end smoke test and README

**Priority:** High | **Effort:** 3h | **Week:** 7
**Labels:** `documentation` `testing`

Full pipeline smoke test and complete project documentation.

**Acceptance Criteria:**

- [ ] Full pipeline runs end-to-end without manual intervention
- [ ] Kafka producer → S3 → Databricks → Redshift → dbt → Streamlit all verified
- [ ] `RUNBOOK.md` documents how to start every service and recover from common failures
- [ ] README includes: project overview, architecture diagram, setup instructions, screenshots, tech stack
- [ ] Demo video (5 min) recorded and linked in README
- [ ] All credentials removed from codebase — `.env.example` is the only reference
- [ ] Project submitted to GitHub before April 29th ✅

-----

## 📊 Summary

|Epic |Tickets|Est. Hours|Week |
|-----------------------|-------|----------|-----------|
|🛠 Project Setup |5 |9h |1 |
|🏗 OOP & Database Layer |7 |14h |2 |
|⚡ Live Crypto Streaming|5 |13h |3 |
|⚙️ Databricks + Spark |4 |11h |4 |
|🏛 Data Warehouse |2 |4h |5 |
|🔧 dbt Modeling |4 |8h |5 |
|🔄 Orchestration |2 |5h |5 |
|🖥 Streamlit Dashboard |3 |7h |6 |
|🤖 AI Integration |2 |5h |6 |
|✅ Polish & Delivery |1 |3h |7 |
|**Total** |**35** |**~79h** |**7 weeks**|

-----

## 🗓 Week-by-Week Calendar

|Week |Dates |Epics |Goal |
|-------|------------|-------------------------|-----------------------------------------|
|Week 1 |Mar 7–14 |Setup |Repo, Docker, AWS, Databricks all working|
|Week 2 |Mar 15–21 |OOP + DB |All 6 classes, CRUD, seeded with AI data |
|Week 3 |Mar 22–28 |Streaming |Live Coinbase prices flowing into S3 |
|Week 4 |Mar 29–Apr 4|Databricks |Delta tables built, time travel working |
|Week 5 |Apr 5–11 |Warehouse + dbt + Airflow|Full warehouse, clean models, DAG running|
|Week 6 |Apr 12–18 |Streamlit + AI |Dashboard live, AI queries working |
|Week 7 |Apr 19–25 |Buffer + Polish |Debugging, README, demo video |
|**Due**|**Apr 29** | |✅ Submit |