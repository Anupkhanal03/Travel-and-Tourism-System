import os
import urllib.request
import pymysql
from db import get_db_connection

def download_and_update():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    images_dir = os.path.join("static", "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Destination mappings: ID -> (URL, filename)
    destinations = {
        5: ("https://images.unsplash.com/photo-1589802829985-817e51171b92?w=800", "annapurna_dest.jpg"),
        6: ("https://images.unsplash.com/photo-1564593457199-b1c4113cb621?w=800", "bardia_dest.jpg"),
        7: ("https://images.unsplash.com/photo-1602002418082-a4443e081dd1?w=800", "lumbini_dest.jpg"),
        8: ("https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800", "rara_dest.jpg"),
        9: ("https://images.unsplash.com/photo-1516084666014-a90b4d45d312?w=800", "bhotekoshi_dest.jpg"),
    }
    
    # Package mappings: ID -> (URL, filename)
    packages = {
        5: ("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800", "annapurna_pkg.jpg"),
        6: ("https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?w=800", "bardia_pkg.jpg"),
        7: ("https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800", "lumbini_pkg.jpg"),
        8: ("https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=800", "rara_pkg.jpg"),
        9: ("https://images.unsplash.com/photo-1530866495561-507c9faab2ed?w=800", "bhotekoshi_pkg.jpg"),
        10: ("https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800", "phewa_pkg.jpg"),
    }
    
    def fetch_image(url, filename):
        filepath = os.path.join(images_dir, filename)
        if not os.path.exists(filepath):
            try:
                # Add a user-agent to bypass basic blocks
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                return False
        return True

    print("Downloading destination images...")
    for dest_id, (url, filename) in destinations.items():
        if fetch_image(url, filename):
            cursor.execute("UPDATE destinations SET image = %s WHERE id = %s", (filename, dest_id))
            
    print("Downloading package images...")
    for pkg_id, (url, filename) in packages.items():
        if fetch_image(url, filename):
            cursor.execute("UPDATE packages SET image = %s WHERE id = %s", (filename, pkg_id))
            
    conn.commit()
    cursor.close()
    conn.close()
    print("Database updated with local image files!")

if __name__ == '__main__':
    download_and_update()
