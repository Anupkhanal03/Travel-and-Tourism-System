import pymysql
from db import get_db_connection

def update_dest_images():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Different images from the packages so they stand out as destinations
    updates = {
        "Annapurna Conservation Area": "https://images.unsplash.com/photo-1589802829985-817e51171b92?w=800",
        "Bardia National Park": "https://images.unsplash.com/photo-1564593457199-b1c4113cb621?w=800",
        "Lumbini": "https://images.unsplash.com/photo-1602002418082-a4443e081dd1?w=800",
        "Rara Lake": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800",
        "Bhotekoshi River": "https://images.unsplash.com/photo-1516084666014-a90b4d45d312?w=800"
    }
    
    for name, img_url in updates.items():
        cursor.execute("UPDATE destinations SET image = %s WHERE name = %s", (img_url, name))
        
    conn.commit()
    cursor.close()
    conn.close()
    print("Successfully assigned distinct destination images.")

if __name__ == '__main__':
    update_dest_images()
