import pymysql
from db import get_db_connection

def dump():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, image FROM destinations")
    dests = cursor.fetchall()
    print("--- DESTINATIONS ---")
    for d in dests:
        print(f"ID: {d['id']} | Name: {d['name']} | Image: {d['image']}")
        
    cursor.execute("SELECT id, title, image FROM packages")
    pkgs = cursor.fetchall()
    print("--- PACKAGES ---")
    for p in pkgs:
        print(f"ID: {p['id']} | Title: {p['title']} | Image: {p['image']}")
        
    cursor.close()
    conn.close()

if __name__ == '__main__':
    dump()
