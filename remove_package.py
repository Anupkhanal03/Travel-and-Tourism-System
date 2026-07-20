import pymysql
from db import get_db_connection

def delete_package():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if bookings depend on this package first and delete them, otherwise foreign key constraint will fail
    cursor.execute("SELECT id FROM packages WHERE title LIKE '%Phewa Lake & Sarangkot Paragliding%'")
    pkg = cursor.fetchone()
    
    if pkg:
        pkg_id = pkg['id']
        cursor.execute("DELETE FROM bookings WHERE package_id = %s", (pkg_id,))
        cursor.execute("DELETE FROM packages WHERE id = %s", (pkg_id,))
        print("Package and associated bookings successfully removed from the database.")
    else:
        print("Package not found.")
        
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    delete_package()
