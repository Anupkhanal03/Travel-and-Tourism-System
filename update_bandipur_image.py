import urllib.request
import os
from db import get_db_connection

# Using a high-quality free Unsplash image for Nepal Village / Bandipur representation
image_url = "https://images.unsplash.com/photo-1544735716-392fe2489ffa?q=80&w=1000"
image_path = "static/images/bandipur_dest.jpg"

try:
    req = urllib.request.Request(
        image_url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    )
    with urllib.request.urlopen(req) as response, open(image_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print("Downloaded Bandipur image successfully.")
except Exception as e:
    print(f"Failed to download image: {e}")

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("SELECT id, image FROM destinations WHERE name LIKE '%%Bandipur%%'")
dests = cursor.fetchall()

print(f"Found destinations: {dests}")

for dest in dests:
    dest_id = dest['id']
    print(f"Updating dest {dest_id}...")
    cursor.execute("UPDATE destinations SET image = 'bandipur_dest.jpg' WHERE id = %s", (dest_id,))
    cursor.execute("UPDATE packages SET image = 'bandipur_dest.jpg' WHERE destination_id = %s", (dest_id,))

conn.commit()
cursor.close()
conn.close()
print("Done updating database.")
