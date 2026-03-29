# Real Estate Listings & Customer Review Analytics System

An end-to-end data analytics project focused on real estate listings and customer reviews. This repository covers the full analytics lifecycle: raw data preparation, feature engineering, PostgreSQL loading, SQL-based business analysis, exploratory notebooks, and Power BI dashboard reporting.

## Business Problem

The objective of this project is to analyze property listings and customer review data to help the business:

- Understand pricing trends
- Identify high-performing listings
- Analyze customer satisfaction
- Improve revenue opportunities and customer experience

## Project Highlights

- Built a reusable data pipeline for listings and reviews data
- Cleaned and standardized raw CSV datasets using Python and Pandas
- Engineered business-focused features such as `price_per_person`, `host_performance_score`, and `review_count`
- Loaded processed data into PostgreSQL for structured analysis
- Wrote SQL queries to answer pricing, performance, and location intelligence questions
- Created Power BI dashboards to communicate insights visually

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- python-dotenv
- SQL
- Jupyter Notebook
- Power BI

## Dataset Summary

Based on the processed data in this repository:

- Listings: `279,712`
- Reviews: `5,373,143`
- Cities covered: `10`
- Neighborhoods covered: `660`
- Average listing price: `608.79`
- Median listing price: `150.00`
- Average review rating: `93.41`

## Repository Structure

```text
.
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- Listings_data_dictionary.csv
|   `-- Reviews_data_dictionary.csv
|-- dashboard/
|   |-- Properties Data Business Insights.pbix
|   |-- Analytics Overview.png
|   |-- Pricing analysis.png
|   |-- Customer Satisfaction.png
|   `-- Location & Performance .png
|-- notebooks/
|   |-- 01_data_exploration.ipynb
|   `-- 02_eda_analysis.ipynb
|-- Reports/
|   |-- Project Overview.pdf
|   `-- Final_Project_Report.md
|-- scripts/
|   |-- data_cleaning.py
|   |-- feature_engineering.py
|   |-- load_to_postgres.py
|   `-- db_connection.py
|-- sql/
|   |-- schema.sql
|   `-- analysis_queries.sql
|-- requirements.txt
`-- README.md
```

## Workflow

### 1. Data Cleaning

[`scripts/data_cleaning.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\data_cleaning.py) performs:

- Duplicate removal
- Price cleaning and numeric conversion
- Date parsing
- Missing value handling
- Column name standardization
- Export of cleaned CSV files to `data/processed/`

### 2. Feature Engineering

[`scripts/feature_engineering.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\feature_engineering.py) creates:

- `price_per_person`
- `host_performance_score`
- `review_count`

These features improve business analysis and dashboard reporting.

### 3. PostgreSQL Loading

[`scripts/load_to_postgres.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\load_to_postgres.py) loads processed data into PostgreSQL tables for downstream SQL analysis.

### 4. SQL Analysis

[`sql/analysis_queries.sql`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\sql\analysis_queries.sql) includes queries for:

- Pricing analysis
- Customer satisfaction analysis
- Listing performance analysis
- Location insights
- Advanced business questions

### 5. Dashboarding

The Power BI file [`dashboard/Properties Data Business Insights.pbix`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Properties Data Business Insights.pbix) provides a visual analytics layer for business stakeholders.

## Key Insights

- The gap between average price and median price indicates a right-skewed pricing distribution with premium listings pulling the average up.
- Hotel rooms have the highest average price among room types.
- Review ratings are generally strong, suggesting high overall customer satisfaction.
- Paris, New York, and Sydney have the largest listing volumes in the dataset.
- Some high-priced listings also have poor ratings, highlighting service and pricing optimization opportunities.

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root with your PostgreSQL credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

## How To Run

Run the pipeline in this order:

### 1. Clean raw data

```powershell
python scripts\data_cleaning.py
```

### 2. Engineer features

```powershell
python scripts\feature_engineering.py
```

### 3. Load processed data into PostgreSQL

```powershell
python scripts\load_to_postgres.py
```

### 4. Execute SQL analysis

Run the queries from [`sql/analysis_queries.sql`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\sql\analysis_queries.sql) in PostgreSQL.

### 5. Open dashboard

Open [`dashboard/Properties Data Business Insights.pbix`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Properties Data Business Insights.pbix) in Power BI Desktop.

## Reports

- Final report: [`Reports/Final_Project_Report.md`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\Reports\Final_Project_Report.md)
- Original overview: [`Reports/Project Overview.pdf`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\Reports\Project Overview.pdf)

## Notes

- The repository includes large processed datasets and dashboard assets.
- The current `requirements.txt` is minimal and may need expansion if this project is prepared for broader reuse or deployment.
- Some existing project files in the workspace were already modified before this README update and were not changed by this README rewrite.

## Author

Data Analytics Project by Shree.
