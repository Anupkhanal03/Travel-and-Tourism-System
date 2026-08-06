import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def update_schema_v2():
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
        print("Adding id_card_photo to guides table...")
        try:
            cursor.execute('ALTER TABLE guides ADD COLUMN id_card_photo VARCHAR(255) DEFAULT NULL')
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1060:
                print("Column id_card_photo already exists.")
            else:
                raise
                
        print("Adding preferred_location to guides table...")
        try:
            cursor.execute('ALTER TABLE guides ADD COLUMN preferred_location VARCHAR(100) DEFAULT NULL')
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1060:
                print("Column preferred_location already exists.")
            else:
                raise

        connection.commit()
        print("Schema update v2 successful!")
        
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    update_schema_v2()
