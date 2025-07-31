import sqlite3
import pandas as pd

# Paths
db_path = 'ecommerce.db'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 1: Create departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
""")

# Step 2: Extract unique categories from products and insert into departments
cursor.execute("SELECT DISTINCT category FROM products")
unique_categories = cursor.fetchall()

for category in unique_categories:
    if category[0]:  # skip NULLs or empty
        cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (category[0],))

# Step 3: Add department_id column to products (if not already added)
cursor.execute("PRAGMA table_info(products)")
columns = [col[1] for col in cursor.fetchall()]
if 'department_id' not in columns:
    cursor.execute("ALTER TABLE products ADD COLUMN department_id INTEGER")

# Step 4: Update department_id in products
cursor.execute("SELECT id, name FROM departments")
department_map = {name: id for id, name in cursor.fetchall()}

for dept_name, dept_id in department_map.items():
    cursor.execute(
        "UPDATE products SET department_id = ? WHERE category = ?",
        (dept_id, dept_name)
    )

# Step 5 (Optional): Create new products table without category
cursor.execute("""
CREATE TABLE IF NOT EXISTS products_new (
    id INTEGER PRIMARY KEY,
    name TEXT,
    brand TEXT,
    cost REAL,
    retail_price REAL,
    department_id INTEGER,
    FOREIGN KEY(department_id) REFERENCES departments(id)
);
""")

# Copy data to new table
cursor.execute("""
INSERT INTO products_new (id, name, brand, cost, retail_price, department_id)
SELECT id, name, brand, cost, retail_price, department_id FROM products;
""")

# Drop old table and rename new one
cursor.execute("DROP TABLE products;")
cursor.execute("ALTER TABLE products_new RENAME TO products;")

# Commit and close
conn.commit()
conn.close()

print("✅ Database refactored: departments table created and products updated with foreign key.")
