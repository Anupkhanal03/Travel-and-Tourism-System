import db

def create_table():
    conn = db.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS package_itineraries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            package_id INT NOT NULL,
            day_number INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
        )
    """)
    
    # We shouldn't TRUNCATE a table with foreign keys unless we disable foreign key checks, 
    # so we'll just DELETE instead.
    cursor.execute("DELETE FROM package_itineraries")
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created and cleared successfully.")

def populate_mock_data():
    conn = db.get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title, duration_days FROM packages")
    packages = cursor.fetchall()
    
    itineraries_to_insert = []
    
    for pkg in packages:
        pkg_id = pkg['id']
        duration = pkg['duration_days']
        title = pkg['title']
        
        for day in range(1, duration + 1):
            if day == 1:
                day_title = f"Arrival and Welcome"
                day_desc = f"Welcome to your first day of the {title} tour! Upon arrival, you'll be greeted by our representative, transferred to your accommodation, and given a brief orientation about the exciting days ahead. Spend the rest of the day relaxing or exploring the nearby area."
            elif day == duration:
                day_title = "Departure and Farewell"
                day_desc = "On the final day, after a hearty breakfast, you'll have some free time for last-minute souvenir shopping or a final stroll. Later, we'll arrange for your transfer back to the airport or your next destination. Have a safe journey!"
            else:
                day_title = f"Exploration Day {day}"
                day_desc = f"Get ready for an action-packed Day {day}! We will start early to make the most of the day. You'll engage in various activities tailored to the {title} package, exploring key landmarks, enjoying local culture, and experiencing the unique highlights of the region."
            
            itineraries_to_insert.append((pkg_id, day, day_title, day_desc))
            
    if itineraries_to_insert:
        cursor.executemany(
            "INSERT INTO package_itineraries (package_id, day_number, title, description) VALUES (%s, %s, %s, %s)",
            itineraries_to_insert
        )
        conn.commit()
        print(f"Inserted {len(itineraries_to_insert)} itinerary days for {len(packages)} packages.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_table()
    populate_mock_data()
