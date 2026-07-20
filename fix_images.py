import shutil, pymysql, os
from db import get_db_connection

def fix_missing_images():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    images_dir = os.path.join("static", "images")
    
    # Use existing local files as substitutes for the broken 404 ones
    shutil.copy(os.path.join(images_dir, 'chitwan.jpg'), os.path.join(images_dir, 'bardia_dest.jpg'))
    shutil.copy(os.path.join(images_dir, 'pokhara.jpg'), os.path.join(images_dir, 'bhotekoshi_dest.jpg'))
    
    cursor.execute("UPDATE destinations SET image = 'bardia_dest.jpg' WHERE id = 6")
    cursor.execute("UPDATE destinations SET image = 'bhotekoshi_dest.jpg' WHERE id = 9")
            
    conn.commit()
    cursor.close()
    conn.close()
    print("Fixed missing images!")

if __name__ == '__main__':
    fix_missing_images()
