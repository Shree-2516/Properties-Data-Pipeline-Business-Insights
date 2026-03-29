# Final Project Report

## Project Assignment

**Project Title:** Real Estate Listings & Customer Review Analytics System

**Business Objective:**  
Analyze property listings and customer reviews to:

- Understand pricing trends
- Identify high-performing listings
- Analyze customer satisfaction
- Help the business improve revenue and customer experience

## 1. Project Overview

This project is a complete data analytics solution built to study real estate listings and customer review behavior across multiple cities. The workflow covers raw data cleaning, feature engineering, PostgreSQL loading, SQL-based business analysis, exploratory analysis in notebooks, and Power BI dashboard reporting.

The final system helps answer key business questions around pricing, listing performance, customer satisfaction, and location-based revenue opportunities.

## 2. Tools and Technologies Used

- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- Jupyter Notebook
- dotenv / SQLAlchemy

## 3. Project Folder Coverage

This report is based on the full project structure:

- `data/`: raw files, processed files, and data dictionaries
- `scripts/`: data cleaning, feature engineering, database connection, and PostgreSQL loading
- `sql/`: schema definition and business analysis queries
- `notebooks/`: exploration and EDA analysis
- `dashboard/`: Power BI dashboard and exported visuals
- `Reports/`: existing `Project Overview.pdf` and this final consolidated report

## 4. Data Pipeline Summary

### Step 1: Data Cleaning

The cleaning pipeline in [`scripts/data_cleaning.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\data_cleaning.py) performs the following work:

- Removes duplicates from listings and reviews
- Cleans the `price` column by removing currency symbols and commas
- Converts numeric and date fields into usable formats
- Fills key missing values such as `price` and `name`
- Standardizes column names to lowercase snake_case
- Saves cleaned outputs into `data/processed/`

### Step 2: Feature Engineering

The feature engineering pipeline in [`scripts/feature_engineering.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\feature_engineering.py) creates business-friendly metrics:

- `price_per_person`
- `host_performance_score`
- `review_count`

These features make later SQL analysis and dashboard storytelling more meaningful.

### Step 3: Database Loading

The loading pipeline in [`scripts/load_to_postgres.py`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\scripts\load_to_postgres.py) reads the processed CSV files and loads them into PostgreSQL tables using SQLAlchemy for analysis and dashboard consumption.

## 5. Database and SQL Analysis

SQL analysis is organized inside [`sql/analysis_queries.sql`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\sql\analysis_queries.sql).

The SQL work covers these business areas:

- Pricing analysis
- Customer satisfaction analysis
- Listing performance analysis
- Location insights
- Advanced business questions

Example question types answered by SQL:

- What is the average listing price?
- Which listings are the most expensive or cheapest?
- Which neighborhoods have the most listings?
- Which locations show the highest revenue potential?
- Which listings have high price but poor ratings?
- Which listings offer the best value?

The schema file [`sql/schema.sql`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\sql\schema.sql) defines the base table structure for listings and reviews.

## 6. Dashboard and Reporting Layer

The dashboard layer is available in:

- [`dashboard/Properties Data Business Insights.pbix`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Properties Data Business Insights.pbix)

Supporting exported dashboard visuals include:

- [`dashboard/Analytics Overview.png`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Analytics Overview.png)
- [`dashboard/Pricing analysis.png`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Pricing analysis.png)
- [`dashboard/Customer Satisfaction.png`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Customer Satisfaction.png)
- [`dashboard/Location & Performance .png`](e:\PROJECTS\Data Analytics\Properties Data Pipeline & Business Insights\dashboard\Location & Performance .png)

These visuals show that the project is not only analytical but also presentation-ready for business users.

## 7. Dataset Summary

Based on the processed project data:

- Total listings: 279,712
- Total reviews: 5,373,143
- Total cities covered: 10
- Total neighborhoods covered: 660
- Total room types analyzed: 4
- Average listing price: 608.79
- Median listing price: 150.00
- Average review rating: 93.41
- Average host performance score: 4.67
- Average price per person: 187.18
- Average reviews per listing: 19.21

## 8. Key Analytical Findings

### Pricing Insights

- The average listing price is 608.79, while the median price is 150.00.
- This large gap suggests the data contains a strong right-skew, meaning a smaller number of premium listings push the average upward.
- Hotel rooms show the highest average price among room types at 800.21.
- Entire places average 673.35, while private rooms average 462.44.

### Customer Satisfaction Insights

- The average review rating is 93.41, which indicates generally high customer satisfaction.
- There are 57,458 listings with perfect or near-perfect recorded ratings.
- Customer review information is strong enough to support quality-based business decisions.

### Performance Insights

- Average reviews per listing are 19.21, showing healthy customer interaction across the platform.
- Engineered features like `host_performance_score` and `review_count` make it easier to identify listings that are both active and highly rated.

### Location Insights

Top cities by listing count:

- Paris: 64,690
- New York: 37,012
- Sydney: 33,630
- Rome: 27,647
- Rio de Janeiro: 26,615

Top neighborhoods by listing volume:

- I Centro Storico: 14,874
- Sydney: 8,074
- Copacabana: 7,712
- Cuauhtemoc: 7,626
- Buttes-Montmartre: 7,237

Top neighborhoods by revenue potential based on summed listing prices:

- Ward 54: 14,922,596
- Cuauhtemoc: 9,284,454
- Vadhana: 6,021,629
- Khlong Toei: 5,958,759
- Ward 115: 5,806,791

### Risk and Opportunity Signals

- There are 949 listings that are both expensive (`price > 200`) and low rated (`review_scores_rating < 60`).
- These listings represent a strong improvement opportunity for pricing strategy, service quality, or listing presentation.

## 9. Business Value of the Project

This project provides business value in several ways:

- Helps understand where pricing is competitive or inflated
- Highlights which listings and hosts are performing well
- Shows where customer satisfaction is strong or weak
- Identifies neighborhoods with strong commercial potential
- Supports business decisions using both SQL and dashboard reporting
- Creates a reusable analytics pipeline for future listing data refreshes

## 10. Final Conclusion

The Real Estate Listings & Customer Review Analytics System successfully delivers a full end-to-end analytics project. It starts from raw listing and review data, transforms the data into analysis-ready form, loads it into PostgreSQL, answers business questions with SQL, and presents insights through a Power BI dashboard.

The project clearly meets the assignment objective by helping the business:

- Understand pricing trends
- Identify high-performing listings
- Analyze customer satisfaction
- Improve both revenue strategy and customer experience

Overall, this is a strong data analytics project because it combines data engineering, SQL analysis, business intelligence, and storytelling in one complete workflow.

## 11. Suggested Viva / Presentation Summary

This project analyzes real estate listings and customer reviews to support pricing, performance, and customer satisfaction decisions. The workflow includes data cleaning in Python, feature engineering, PostgreSQL loading, SQL analysis, and Power BI dashboard creation. The processed dataset contains 279,712 listings and more than 5.3 million reviews across 10 cities. Key results show strong pricing variation, generally high customer ratings, and several high-revenue neighborhoods with strong business potential.
