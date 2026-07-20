import shutil, os, pymysql
from db import get_db_connection

def fix_all_images():
    images_dir = os.path.join("static", "images")
    brain_dir = r"C:\Users\Acer\.gemini\antigravity-ide\brain\7eb782fc-c263-4380-954d-5e2390dc2630"
    
    # 1. Apply the new AI generated images for the destinations
    shutil.copy(os.path.join(brain_dir, 'annapurna_dest_new_1782207631525.png'), os.path.join(images_dir, 'annapurna_dest.png'))
    shutil.copy(os.path.join(brain_dir, 'lumbini_dest_new_1782207642885.png'), os.path.join(images_dir, 'lumbini_dest.png'))
    shutil.copy(os.path.join(brain_dir, 'rara_dest_new_1782207653773.png'), os.path.join(images_dir, 'rara_dest.png'))
    
    # 2. Apply the AI generated image for Annapurna package
    shutil.copy(os.path.join(brain_dir, 'annapurna_pkg_new_1782207664990.png'), os.path.join(images_dir, 'annapurna_pkg.png'))
    
    # 3. For the other packages that might be broken, substitute them with guaranteed working local images
    shutil.copy(os.path.join(images_dir, 'chitwan_pkg.jpg'), os.path.join(images_dir, 'bardia_pkg.jpg'))
    shutil.copy(os.path.join(images_dir, 'lumbini_dest.png'), os.path.join(images_dir, 'lumbini_pkg.png'))
    shutil.copy(os.path.join(images_dir, 'rara_dest.png'), os.path.join(images_dir, 'rara_pkg.png'))
    shutil.copy(os.path.join(images_dir, 'bhotekoshi_dest.png'), os.path.join(images_dir, 'bhotekoshi_pkg.png'))
    shutil.copy(os.path.join(images_dir, 'pokhara_pkg.jpg'), os.path.join(images_dir, 'phewa_pkg.jpg'))
    
    # 4. Update the Database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Destinations update
    cursor.execute("UPDATE destinations SET image = 'annapurna_dest.png' WHERE name = 'Annapurna Conservation Area'")
    cursor.execute("UPDATE destinations SET image = 'lumbini_dest.png' WHERE name = 'Lumbini'")
    cursor.execute("UPDATE destinations SET image = 'rara_dest.png' WHERE name = 'Rara Lake'")
    
    # Packages update
    cursor.execute("UPDATE packages SET image = 'annapurna_pkg.png' WHERE title LIKE 'Annapurna%'")
    cursor.execute("UPDATE packages SET image = 'bardia_pkg.jpg' WHERE title LIKE 'Bardia%'")
    cursor.execute("UPDATE packages SET image = 'lumbini_pkg.png' WHERE title LIKE 'Buddhist Heritage%'")
    cursor.execute("UPDATE packages SET image = 'rara_pkg.png' WHERE title LIKE 'Rara Wilderness%'")
    cursor.execute("UPDATE packages SET image = 'bhotekoshi_pkg.png' WHERE title LIKE 'Bhotekoshi%'")
    cursor.execute("UPDATE packages SET image = 'phewa_pkg.jpg' WHERE title LIKE 'Phewa Lake%'")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("All requested images fixed successfully!")

if __name__ == '__main__':
    fix_all_images()
