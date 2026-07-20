from db import get_db_connection

def add_reviews_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            package_id INT NOT NULL,
            rating INT NOT NULL,
            review_text TEXT,
            sentiment VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
        )
    """)
    
    print("Successfully added reviews table.")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_reviews_table()
