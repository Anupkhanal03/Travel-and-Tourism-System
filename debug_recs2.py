import pandas as pd
from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

query_all_pkgs = "SELECT p.id, p.title, p.price, p.duration_days, p.image FROM packages p JOIN destinations d ON p.destination_id = d.id"
cursor.execute(query_all_pkgs)
data_pkgs = cursor.fetchall()
df_pkgs = pd.DataFrame(data_pkgs) if data_pkgs else pd.DataFrame()

print("df_pkgs empty?", df_pkgs.empty)

query_popularity = "SELECT package_id, COUNT(*) as booking_count FROM bookings WHERE status != 'Cancelled' GROUP BY package_id ORDER BY booking_count DESC"
cursor.execute(query_popularity)
data_pop = cursor.fetchall()
df_pop = pd.DataFrame(data_pop) if data_pop else pd.DataFrame()
popular_ids = df_pop['package_id'].tolist() if not df_pop.empty else []

print("popular_ids:", popular_ids)

added_ids = set()
all_pkg_ids_ordered = popular_ids + [pid for pid in df_pkgs['id'].tolist() if pid not in popular_ids]

print("all_pkg_ids_ordered:", all_pkg_ids_ordered)

recommended_packages = []
for pid in all_pkg_ids_ordered:
    if pid not in added_ids:
        print(f"Checking pid: {pid}")
        try:
            row = df_pkgs[df_pkgs['id'] == pid].iloc[0]
            print(f"Row found: {row['title']}")
            recommended_packages.append(row['title'])
        except Exception as e:
            print(f"Error for pid {pid}: {e}")

print("final recommendations:", len(recommended_packages))
