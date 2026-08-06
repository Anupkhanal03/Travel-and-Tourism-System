import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def update_schema_v3():
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
        print("Adding status to guides table...")
        try:
            cursor.execute("ALTER TABLE guides ADD COLUMN status VARCHAR(20) DEFAULT 'Pending'")
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1060:
                print("Column status already exists.")
            else:
                raise
                
        # Also update any existing guides to be 'Approved' so we don't break existing ones
        cursor.execute("UPDATE guides SET status = 'Approved' WHERE status = 'Pending' AND id_card_photo IS NULL")

        connection.commit()
        print("Schema update v3 successful!")
        
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    update_schema_v3()
