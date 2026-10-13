# SWYNEX – End-to-End Data Analytics Project

## 1. Project Overview

This project was completed as part of my SWYNEX internship and demonstrates a data analytics workflow using the Online Retail transaction dataset.

The project covers data quality assessment, data cleaning, data preparation, sales analysis, and interactive dashboard development using Python, Pandas, and Microsoft Power BI.

The goal is to transform raw retail transaction data into a reliable dataset and present sales performance in a clear, interactive dashboard to support business decision-making.

## 2. Problem Statement

Retail businesses generate large volumes of transaction data, but inaccurate, incomplete, or inconsistent records can affect reporting and business decisions.

The objective of this project is to identify and resolve data quality issues in an online retail dataset, prepare the data for analysis, and develop an interactive Power BI dashboard to explore revenue, orders, customers, products, and geographical sales performance.

## 3. Dataset Information

- **Dataset:** Online Retail
- **Source:** UCI Machine Learning Repository
- **Original records:** 541,909 rows
- **Original columns:** 8
- **Final records:** 534,129 rows
- **Final columns:** 9

The dataset contains online retail transactions with information such as invoice number, product code, product description, quantity, invoice date, unit price, customer ID, and country.

An additional Revenue column was created during data preparation.

## 4. Tools and Technologies

- Python
- Pandas
- OpenPyXL
- Microsoft Excel
- Microsoft Power BI
- GitHub

## 5. Data Quality Issues Identified

The initial data quality assessment identified the following issues:

- 5,268 duplicate records
- 1,454 records with missing product descriptions
- Missing customer IDs
- Zero or negative unit prices
- Inconsistent data types
- Unnecessary whitespace in text fields

## 6. Data Cleaning and Preparation

### Step 1: Duplicate Removal

Identified and removed 5,268 duplicate records to prevent repeated transactions from affecting the analysis.

### Step 2: Missing Product Descriptions

Removed 1,454 records where the Description field was missing.

### Step 3: Missing Customer IDs

Replaced missing CustomerID values with "Unknown" so that records without an identified customer could be retained for appropriate analysis.

A total of 133,583 missing CustomerID values were handled after duplicate removal.

### Step 4: Data Type Standardization

- Converted InvoiceDate to datetime format.
- Converted Quantity to numeric format.
- Converted UnitPrice to numeric format.
- Standardized identifier fields as text.

### Step 5: Text Standardization

Removed unnecessary whitespace from Description, Country, StockCode, and InvoiceNo fields.

### Step 6: Invalid Unit Prices

Removed 1,058 records where UnitPrice was zero or negative.

### Step 7: Quantity Validation

Checked for zero-quantity records; none were found in the assessed dataset.

Negative quantities were retained because they can represent returns or cancelled transactions and should be considered appropriately during sales analysis.

### Step 8: Revenue Calculation

Created a Revenue column using the following formula:

`Revenue = Quantity × UnitPrice`

This field supports revenue calculations and product, country, and time-based analysis.

## 7. Final Dataset Summary

| Data quality measure | Result |
|---|---:|
| Original rows | 541,909 |
| Duplicate records removed | 5,268 |
| Missing-description records removed | 1,454 |
| Invalid-price records removed | 1,058 |
| Final rows | 534,129 |
| Final columns | 9 |

The final dataset contains no remaining duplicate records or missing values according to the cleaning validation performed. Missing customer IDs were represented as "Unknown".

The cleaned dataset is prepared for further sales analysis and visualization.

## 8. Exploratory and Business Analysis

The prepared dataset was used to support sales analysis through Microsoft Power BI.

The analysis focuses on:

- Overall revenue performance
- Total quantity sold
- Order volume
- Customer coverage
- Revenue trends over time
- Product-level revenue comparisons
- Country-level revenue comparisons

These views help explore sales patterns, compare performance across categories, and identify areas for further business investigation.

## 9. Interactive Power BI Dashboard

An interactive sales dashboard was developed in Microsoft Power BI.

### Key Performance Indicators

- Total Revenue
- Total Quantity
- Total Orders
- Total Customers

### Dashboard Visualizations

- Revenue trend over time
- Product revenue analysis
- Revenue by country
- Country selection for interactive exploration
- Date-based filtering

The dashboard allows users to explore sales performance across different dates, products, and countries.

### Dashboard Screenshot

Add your actual dashboard screenshot to the `screenshots` folder and use the correct filename in the image link below.

![SWYNEX Interactive Power BI Dashboard](screenshots/dashboard_screenshot.png)

### Power BI File

The Power BI report is available in the repository as:

`SWYNEX_Interactive_Dashboard.pbix`

Open the file in Microsoft Power BI Desktop to interact with the report, provided the file has been uploaded to the repository.

## 10. Key Business Insights

The dashboard is designed to help answer important business questions:

1. **Revenue performance:** How does revenue change over time?
2. **Product performance:** Which products contribute the most revenue?
3. **Geographical performance:** Which countries generate the highest revenue?
4. **Order activity:** How do order volumes change across the selected periods?
5. **Customer coverage:** How many customers are represented in the transaction data?

The actual top-performing products, countries, revenue figures, and time periods should be documented from the dashboard results. These findings can help businesses prioritize product performance reviews, explore geographical opportunities, and investigate changes in sales trends.

## 11. Project Structure

```text
SWYNEX-data-cleaning-preparation/
├── raw_data/
│   └── Online Retail.xlsx
├── cleaned_data/
│   └── cleaned_online_retail.csv
├── python/
│   └── data_cleaning.py
├── screenshots/
│   └── dashboard_screenshot.png
├── SWYNEX_Interactive_Dashboard.pbix
└── README.md
```

The structure above describes the intended project organization. File names and locations should match the actual contents of the repository.

## 12. Key Learnings

Through this project, I gained practical experience in:

- Assessing data quality
- Cleaning and transforming data with Python and Pandas
- Handling missing values and duplicate records
- Standardizing data types
- Creating calculated columns for analysis
- Developing interactive Power BI dashboards
- Communicating analytical findings through visualizations
- Managing project files and documentation using GitHub

## 13. Conclusion

This project demonstrates an end-to-end data analytics workflow, from raw data preparation to interactive business reporting.

The cleaning process improved the consistency and usability of the Online Retail dataset, while the Power BI dashboard provides a visual approach to exploring revenue, orders, products, customers, and geographical performance.

The project strengthened my practical skills in Python, data preparation, Power BI, data visualization, and business-oriented analysis.

## 14. Acknowledgment

This project was completed as part of my SWYNEX internship. The Online Retail dataset is sourced from the UCI Machine Learning Repository.

**Technologies:** Python | Pandas | Excel | Power BI | GitHub

**Project Repository:**  
https://github.com/gunapriyasadhu02/SWYNEX-data-cleaning-preparation
