import pandas as pd

# ==========================================
# SWYNEX - Data Cleaning & Preparation
# ==========================================

# Load raw dataset
df = pd.read_excel("raw_data/Online Retail.xlsx")

print("===== ORIGINAL DATASET =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ------------------------------------------
# 1. Remove duplicate records
# ------------------------------------------
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicates_before)

# ------------------------------------------
# 2. Clean text columns
# ------------------------------------------
df["Description"] = df["Description"].astype("string").str.strip()
df["Country"] = df["Country"].astype("string").str.strip()
df["StockCode"] = df["StockCode"].astype("string").str.strip()
df["InvoiceNo"] = df["InvoiceNo"].astype("string").str.strip()

# ------------------------------------------
# 3. Convert data types
# ------------------------------------------
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"],
    errors="coerce"
)

# CustomerID is treated as text because it is an identifier
df["CustomerID"] = df["CustomerID"].astype("string").str.strip()

# ------------------------------------------
# 4. Handle missing Description
# ------------------------------------------
missing_description = df["Description"].isna().sum()

df = df.dropna(subset=["Description"])

print("Rows removed due to missing Description:",
      missing_description)

# ------------------------------------------
# 5. Handle missing CustomerID
# ------------------------------------------
missing_customer = df["CustomerID"].isna().sum()

df["CustomerID"] = df["CustomerID"].fillna("Unknown")

print("Missing CustomerID values replaced with 'Unknown':",
      missing_customer)

# ------------------------------------------
# 6. Remove invalid values
# ------------------------------------------

# Remove rows where UnitPrice is zero or negative
invalid_price = (df["UnitPrice"] <= 0).sum()

df = df[df["UnitPrice"] > 0]

print("Invalid UnitPrice rows removed:", invalid_price)

# Remove rows where Quantity is zero
invalid_quantity = (df["Quantity"] == 0).sum()

df = df[df["Quantity"] != 0]

print("Zero Quantity rows removed:", invalid_quantity)

# ------------------------------------------
# 7. Remove rows with invalid dates
# ------------------------------------------
invalid_dates = df["InvoiceDate"].isna().sum()

df = df.dropna(subset=["InvoiceDate"])

print("Invalid dates removed:", invalid_dates)

# ------------------------------------------
# 8. Create Revenue column
# ------------------------------------------
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# ------------------------------------------
# 9. Save cleaned dataset
# ------------------------------------------
output_file = "cleaned_data/cleaned_online_retail.csv"

df.to_csv(output_file, index=False)

# ------------------------------------------
# 10. Final quality report
# ------------------------------------------
print("\n===== CLEANED DATASET =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nRemaining duplicate rows:")
print(df.duplicated().sum())

print("\nCleaned dataset saved to:")
print(output_file)

print("\n===== CLEANING COMPLETED =====")