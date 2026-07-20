import pandas as pd
from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

query = """
    SELECT p.id AS id, p.title, p.description, p.price, p.duration_days, p.image, 
           d.name AS dest_name, d.category AS dest_category, d.location AS dest_location
    FROM packages p
    JOIN destinations d ON p.destination_id = d.id
"""
cursor.execute(query)
data = cursor.fetchall()
df = pd.DataFrame(data)
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("id column:", df['id'].tolist())
print("First row:", df.iloc[0].to_dict())

# Check if filtering works
pid = df['id'].tolist()[0]
match = df[df['id'] == pid]
print("Match for first pid:", len(match))
