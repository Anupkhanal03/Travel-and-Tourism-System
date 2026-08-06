import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def update_schema():
    print("Connecting to DB...")
    connection = pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),           
        password=os.environ.get('DB_PASSWORD', ''),           
        database=os.environ.get('DB_NAME', 'nepal_travel_db'),
        port=int(os.environ.get('DB_PORT', 3306))
    )
    
    cursor = connection.cursor()
    
    try:
        print("Creating guides table...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guides (
                id INT AUTO_INCREMENT PRIMARY KEY,
                full_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                experience_years INT DEFAULT 0,
                languages VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        print("Adding guide_id to bookings table...")
        try:
            cursor.execute('''
                ALTER TABLE bookings 
                ADD COLUMN guide_id INT DEFAULT NULL,
                ADD FOREIGN KEY (guide_id) REFERENCES guides(id) ON DELETE SET NULL
            ''')
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1060:
                print("Column guide_id already exists in bookings.")
            else:
                raise
                
        print("Creating guide_notifications table...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guide_notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                guide_id INT NOT NULL,
                booking_id INT NOT NULL,
                message TEXT NOT NULL,
                is_read BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (guide_id) REFERENCES guides(id) ON DELETE CASCADE,
                FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE
            )
        ''')
        
        connection.commit()
        print("Schema update successful!")
        
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    update_schema()
