import db

def generate_day_details(day, duration, title, destination):
    title_lower = title.lower()
    dest_lower = destination.lower()
    
    is_trek = 'trek' in title_lower or 'base camp' in title_lower or 'circuit' in title_lower or 'poon hill' in dest_lower or 'gosainkunda' in dest_lower
    is_safari = 'safari' in title_lower or 'jungle' in title_lower or 'national park' in dest_lower or 'bardia' in dest_lower
    
    # 1-day tours
    if duration == 1:
        return (f"Full Day {destination} Experience", 
                f"Make the most of your day exploring the highlights of {destination}. The day will be packed with exciting activities and immersive experiences tailored to {title}, culminating in a beautiful evening before wrapping up.")
    
    # First Day
    if day == 1:
        if is_trek:
            return ("Arrival, Briefing & Preparation", 
                    f"Welcome to Nepal! Upon arrival for your {title}, our team will receive you. We'll have a pre-trek briefing, check all necessary permits and gear, and rest up for the adventure starting tomorrow.")
        elif is_safari:
            return ("Welcome to the Jungle & Evening Walk", 
                    f"Upon reaching {destination}, check into the resort. Enjoy a welcome drink followed by an evening walk around the local villages or a peaceful sunset view over the river.")
        else:
            return ("Arrival & Hotel Transfer", 
                    f"Welcome to {destination}! You will be transferred to your comfortable accommodation. The rest of the day is free for you to relax, wander the vibrant local streets, and get a feel for the local atmosphere.")
            
    # Last Day
    if day == duration:
        if is_trek:
            return ("Final Departure or Onward Journey", 
                    "It's time to say goodbye! After a final hearty breakfast, we will arrange your transfer to the airport or your next destination. Take home unforgettable memories of the Himalayas.")
        else:
            return ("Morning Activity & Departure", 
                    "Enjoy your final breakfast with a beautiful view. You may have some time for last-minute souvenir shopping before we assist you with your departure. Have a safe journey!")
            
    # Second Day (often travel/starting point)
    if day == 2 and duration > 3:
        if is_trek:
            return ("Journey to the Trailhead", 
                    "Today we take a scenic drive or a thrilling short flight to the starting point of our trek. We'll begin our first short hike, walking alongside lush green valleys and beautiful rivers.")
            
    # Acclimatization (for long treks)
    if is_trek and duration >= 10 and day == 5:
        return ("Acclimatization and Rest Day", 
                "To ensure a safe and enjoyable journey, today is dedicated to acclimatization. We'll take a short hike to a higher viewpoint and return to our lodge to let our bodies adjust to the altitude. Enjoy the spectacular panoramic mountain views!")

    # The Climax Day
    if is_trek and day == (duration - 3) and duration >= 7:
        return ("Reaching the Ultimate Destination", 
                "Today is the big day! We push forward to reach the highest point or the main highlight of the trek. The trail might be challenging, but the close-up, breathtaking views of the majestic peaks will make it totally worth it.")

    # Generic Intermediate Days
    if is_trek:
        activities = [
            "Trekking through dense rhododendron and oak forests, crossing thrilling suspension bridges over roaring rivers.",
            "Ascending steeper trails while passing through traditional mountain villages, interacting with friendly locals.",
            "Enjoying a relatively gentle walk with stunning views of snow-capped peaks continuously in the backdrop.",
            "Navigating through rocky terrains and glacial moraines as the vegetation starts to thin out at higher altitudes.",
            "Descending through beautiful valleys, retracing our steps with a new perspective on the majestic landscapes."
        ]
        titles = [
            "Trek through Scenic Trails",
            "Ascent to Higher Altitudes",
            "Exploring Mountain Villages",
            "Traversing the Glacial Valleys",
            "Descending Through Lush Forests"
        ]
        idx = (day - 2) % len(activities)
        return (titles[idx], activities[idx])
        
    elif is_safari:
        activities = [
            "Embark on a thrilling jungle safari deep into the national park. Keep an eye out for rhinos, deer, and if lucky, the elusive Royal Bengal Tiger.",
            "Enjoy a serene canoe ride down the river, spotting crocodiles and exotic birds, followed by a guided jungle walk.",
            "Visit the elephant breeding center and take a cultural tour of the indigenous Tharu village to experience their rich traditions."
        ]
        titles = [
            "Wildlife Safari Adventure",
            "Canoe Ride & Jungle Walk",
            "Cultural Village Tour"
        ]
        idx = (day - 2) % len(activities)
        return (titles[idx], activities[idx])
        
    else: # Cultural / City
        activities = [
            "Visit ancient temples, historical monuments, and UNESCO World Heritage Sites, soaking in the rich cultural history.",
            "A day dedicated to exploring local markets, interacting with artisans, and trying authentic local delicacies.",
            "A scenic drive to nearby hill stations or viewpoints to catch a mesmerizing sunrise over the mountains.",
            "Enjoying guided heritage walks through narrow alleys, discovering hidden courtyards and ancient architecture."
        ]
        titles = [
            "Heritage & Cultural Tour",
            "Local Markets & Cuisine",
            "Scenic Viewpoints",
            "Guided City Walk"
        ]
        idx = (day - 2) % len(activities)
        return (titles[idx], activities[idx])

def update_itineraries():
    conn = db.get_db_connection()
    cursor = conn.cursor()
    
    # Clear existing itineraries
    cursor.execute("DELETE FROM package_itineraries")
    
    cursor.execute('''
        SELECT p.id, p.title, p.duration_days, d.name as destination 
        FROM packages p 
        JOIN destinations d ON p.destination_id = d.id
    ''')
    packages = cursor.fetchall()
    
    itineraries_to_insert = []
    
    for pkg in packages:
        pkg_id = pkg['id']
        duration = pkg['duration_days']
        title = pkg['title']
        destination = pkg['destination']
        
        for day in range(1, duration + 1):
            day_title, day_desc = generate_day_details(day, duration, title, destination)
            itineraries_to_insert.append((pkg_id, day, day_title, day_desc))
            
    if itineraries_to_insert:
        cursor.executemany(
            "INSERT INTO package_itineraries (package_id, day_number, title, description) VALUES (%s, %s, %s, %s)",
            itineraries_to_insert
        )
        conn.commit()
        print(f"Updated {len(itineraries_to_insert)} exciting itinerary days for {len(packages)} packages.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_itineraries()
