import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='@Anup.03',
        database='nepal_travel_db',
        cursorclass=pymysql.cursors.DictCursor
    )

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact_messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
cursor.close()
conn.close()
print("Table created successfully")
