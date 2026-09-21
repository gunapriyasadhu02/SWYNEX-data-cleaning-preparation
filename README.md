\# SWYNEX - Data Cleaning \& Preparation



\## Project Overview



This project focuses on cleaning and preparing a public

Online Retail transaction dataset for further analysis.



The objective was to identify and resolve common data-quality

issues including duplicate records, missing values, invalid

values, and data-type inconsistencies.



\## Dataset



Dataset: Online Retail



Source:

UCI Machine Learning Repository



Original Dataset:

\- Rows: 541,909

\- Columns: 8



\## Tools Used



\- Python

\- Pandas

\- OpenPyXL

\- Excel

\- GitHub



\## Data Quality Issues Identified



The following issues were identified during the initial

data-quality assessment:



\- 5,268 duplicate records

\- 1,454 missing Description values

\- Missing CustomerID values

\- Invalid UnitPrice values

\- Data-type inconsistencies requiring standardization



\## Data Cleaning Performed



\### 1. Duplicate Records



Removed 5,268 duplicate records.



\### 2. Missing Description



Removed 1,454 records where the Description field was missing.



\### 3. Missing CustomerID



Missing CustomerID values were replaced with `Unknown`.



A total of 133,583 missing CustomerID values were handled

after duplicate records were removed.



\### 4. Data Type Standardization



\- InvoiceDate converted to datetime

\- Quantity converted to numeric

\- UnitPrice converted to numeric

\- Identifier fields standardized as text



\### 5. Text Standardization



Whitespace was removed from:



\- Description

\- Country

\- StockCode

\- InvoiceNo



\### 6. Invalid UnitPrice



Removed 1,058 records where UnitPrice was zero or negative.



\### 7. Quantity Validation



Zero-quantity records were checked.

No zero-quantity records were found.



Negative quantities were retained because they can represent

returns or cancelled transactions.



\### 8. Revenue Calculation



A new Revenue column was created:



Revenue = Quantity × UnitPrice



\## Final Dataset



After cleaning:



\- Rows: 534,129

\- Columns: 9

\- Missing values: 0

\- Duplicate records: 0



\## Project Structure



```text

SWYNEX-data-cleaning-preparation/

│

├── raw\_data/

│   └── Online Retail.xlsx

│

├── cleaned\_data/

│   └── cleaned\_online\_retail.csv

│

├── python/

│   └── data\_cleaning.py

│

├── screenshots/

│

└── README.md

Conclusion



The raw Online Retail dataset was successfully cleaned and

prepared for further data analysis. The cleaning process

improved data consistency, removed duplicate and invalid

records, handled missing values, standardized data types,

and created a Revenue field for future analysis.

