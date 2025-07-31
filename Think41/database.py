import pandas as pd
import sqlite3

# Define paths
csv_file_path = r'C:\Users\Anant\OneDrive\Desktop\think41\Think41\products.csv'
sqlite_db_path = 'ecommerce.db'  # SQLite DB file

# Step 1: Read CSV directly from file system
df = pd.read_csv(csv_file_path)

# Optional: clean column names
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

# Step 2: Connect to SQLite and create table
conn = sqlite3.connect(sqlite_db_path)

# Step 3: Write DataFrame to SQLite table
df.to_sql('products', conn, if_exists='replace', index=False)

print("✅ products.csv has been loaded into ecommerce.db (table: products)")

# ✅ Step 4: Query and display the first 5 rows from the table
result_df = pd.read_sql_query("SELECT * FROM products LIMIT 5;", conn)

print("\n📦 Preview of 'products' table:")
print(result_df)

# Step 5: Close the database connection
conn.close()
