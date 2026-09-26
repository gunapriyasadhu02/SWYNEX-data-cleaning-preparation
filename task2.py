# ==========================================
# SWYNEX - TASK 2: EXPLORATORY DATA ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------
# 1. Load the cleaned dataset
# ------------------------------------------

project_folder = Path(__file__).resolve().parent
cleaned_folder = project_folder / "cleaned_data"

csv_files = list(cleaned_folder.glob("cleaned_data.csv"))

if not csv_files:
    print("No CSV file found in the cleaned_data folder.")
    exit()

file_path = csv_files[0]

cleaned_df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("File:", file_path.name)

# ------------------------------------------
# 2. Basic information
# ------------------------------------------

print("\n========== DATASET SHAPE ==========")
print(cleaned_df.shape)

print("\n========== COLUMNS ==========")
print(cleaned_df.columns)

print("\n========== DATA TYPES ==========")
print(cleaned_df.dtypes)

# ------------------------------------------
# 3. Create Sales column
# ------------------------------------------

cleaned_df["Sales"] = (
    cleaned_df["Quantity"] * cleaned_df["UnitPrice"]
)

print("\nSales column created successfully!")

# ------------------------------------------
# 4. Total Sales
# ------------------------------------------

total_sales = cleaned_df["Sales"].sum()

print("\n========== TOTAL SALES ==========")
print(f"Total Sales: £{total_sales:,.2f}")

# ------------------------------------------
# 5. Top 10 countries by sales
# ------------------------------------------

top_countries = (
    cleaned_df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 COUNTRIES BY SALES ==========")
print(top_countries)

# ------------------------------------------
# 6. Plot top 10 countries
# ------------------------------------------

plt.figure(figsize=(10, 5))

top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Sales")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# ------------------------------------------
# 7. Top 10 products by quantity sold
# ------------------------------------------

top_products = (
    cleaned_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY QUANTITY ==========")
print(top_products)

# ------------------------------------------
# 8. Plot top 10 products
# ------------------------------------------

plt.figure(figsize=(10, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")

plt.tight_layout()
plt.show()

# ------------------------------------------
# 9. Sales by country - summary
# ------------------------------------------

country_summary = (
    cleaned_df.groupby("Country")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Number_of_Orders=("InvoiceNo", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== COUNTRY SALES SUMMARY ==========")
print(country_summary.head(10))

# ------------------------------------------
# 10. Final Task 2 message
# ------------------------------------------

print("\n==========================================")
print("TASK 2 EDA COMPLETED SUCCESSFULLY!")
print("==========================================")