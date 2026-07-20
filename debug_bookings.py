import pandas as pd
from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# Check user 2's bookings
cursor.execute("SELECT * FROM bookings WHERE user_id = 2")
bookings = cursor.fetchall()
print(f"Deepa (user_id=2) has {len(bookings)} bookings")
for b in bookings:
    print(f"  - pkg_id: {b['package_id']}, status: {b['status']}")

# Check all bookings for popularity
cursor.execute("SELECT package_id, COUNT(*) as cnt FROM bookings WHERE status != 'Cancelled' GROUP BY package_id ORDER BY cnt DESC")
pop = cursor.fetchall()
print("\nAll booking popularity:")
for p in pop:
    print(f"  pkg {p['package_id']}: {p['cnt']} bookings")
