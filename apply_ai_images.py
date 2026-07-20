import shutil, pymysql
from db import get_db_connection

def apply_ai_images():
    shutil.copy(r'C:\Users\Acer\.gemini\antigravity-ide\brain\7eb782fc-c263-4380-954d-5e2390dc2630\bardia_dest_1782207304018.png', 'static/images/bardia_dest.png')
    shutil.copy(r'C:\Users\Acer\.gemini\antigravity-ide\brain\7eb782fc-c263-4380-954d-5e2390dc2630\bhotekoshi_dest_1782207314795.png', 'static/images/bhotekoshi_dest.png')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE destinations SET image = 'bardia_dest.png' WHERE name = 'Bardia National Park'")
    cursor.execute("UPDATE destinations SET image = 'bhotekoshi_dest.png' WHERE name = 'Bhotekoshi River'")
    conn.commit()
    cursor.close()
    conn.close()
    print("AI images applied successfully!")

if __name__ == '__main__':
    apply_ai_images()
