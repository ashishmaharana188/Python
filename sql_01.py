import sqlite3
import pandas as pd

connection = sqlite3.connect("temporary.db")
cursor = connection.cursor()


cursor.execute(
    """
CREATE TABLE IF NOT EXISTS insurance (
    id INTEGER PRIMARY KEY,
    age INTEGER,
    sex TEXT,
    bmi FLOAT,
    children INTEGER,
    smoker BOOLEAN,
    region TEXT,
    charges FLOAT
)
"""
)


files = {"insurance": "insurance.csv"}

for table_name, file_path in files.items():

    df = pd.read_csv(file_path)
    print(df.head())


cursor.execute("SELECT * FROM insurance")

result = cursor.fetchall()

print(result)
