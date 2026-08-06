import pymysql
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import json

load_dotenv()

def create_dummy_guides():
    connection = pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),           
        password=os.environ.get('DB_PASSWORD', ''),           
        database=os.environ.get('DB_NAME', 'nepal_travel_db'),
        port=int(os.environ.get('DB_PORT', 3306)),
        cursorclass=pymysql.cursors.DictCursor
    )
    
    cursor = connection.cursor()
    
    # Get unique destinations that have packages
    cursor.execute('''
        SELECT DISTINCT d.name 
        FROM destinations d
        JOIN packages p ON d.id = p.destination_id
    ''')
    destinations = [row['name'] for row in cursor.fetchall()]
    
    credentials = []
    
    try:
        # Create 2 guides per destination
        password_plain = "password123"
        hashed_password = generate_password_hash(password_plain, method='pbkdf2:sha256')
        
        for i, dest in enumerate(destinations):
            for j in range(1, 3):
                name = f"{dest.split()[0]} Guide {j}"
                email = f"guide{j}_{i}@example.com"
                
                # Check if exists
                cursor.execute('SELECT id FROM guides WHERE email = %s', (email,))
                if not cursor.fetchone():
                    cursor.execute('''
                        INSERT INTO guides 
                        (full_name, email, password_hash, phone, experience_years, languages, preferred_location, status) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 'Approved')
                    ''', (name, email, hashed_password, "9800000000", 5, "English, Nepali", dest))
                    
                    credentials.append({
                        "Location": dest,
                        "Name": name,
                        "Email": email,
                        "Password": password_plain
                    })
        
        connection.commit()
        
        with open('dummy_guides.json', 'w') as f:
            json.dump(credentials, f)
            
        print("Dummy guides created successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    create_dummy_guides()
