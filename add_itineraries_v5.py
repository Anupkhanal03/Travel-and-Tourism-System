import db

DESTINATION_KNOWLEDGE = {
    "pokhara": [
        ("Sarangkot", "Watch a breathtaking sunrise.", 28.2439, 83.9472),
        ("Fewa Lake", "Enjoy a peaceful boat ride.", 28.2096, 83.9556),
        ("World Peace Pagoda", "Hike up to the Shanti Stupa.", 28.1963, 83.9431),
        ("Davis Falls & Gupteshwor Cave", "Witness the mysterious underground waterfall.", 28.1895, 83.9577),
        ("Begnas Lake", "Take a day trip to the quieter lake.", 28.1691, 84.0931),
        ("International Mountain Museum", "Learn about the history of mountaineering.", 28.1887, 83.9782)
    ],
    "chitwan": [
        ("Rapti River", "Enjoy a serene canoe ride at dawn.", 27.5683, 84.4842),
        ("Deep Jungle (Core Area)", "Embark on a thrilling jeep safari.", 27.5341, 84.4525),
        ("Tharu Village", "Experience the rich culture.", 27.5750, 84.4950),
        ("Elephant Breeding Center", "Visit the center to see baby elephants.", 27.5925, 84.4716),
        ("Bishazari Tal (20,000 Lakes)", "Explore this wetland area.", 27.6045, 84.4532)
    ],
    "everest": [
        ("Lukla & Phakding", "Experience a thrilling flight.", 27.7397, 86.7208), # Phakding
        ("Namche Bazaar", "Hike up to Namche, the vibrant Sherpa capital.", 27.8069, 86.7140),
        ("Tengboche Monastery", "Visit the largest gompa in the Khumbu region.", 27.8361, 86.7644),
        ("Dingboche", "Trek through alpine meadows to reach Dingboche.", 27.8925, 86.8306),
        ("Lobuche", "Navigate the rugged glacial moraines.", 27.9483, 86.8108),
        ("Gorakshep", "Arrive at the last outpost before the Base Camp.", 27.9806, 86.8286),
        ("Everest Base Camp", "Reach the legendary Base Camp!", 28.0026, 86.8526),
        ("Kala Patthar", "Wake up before dawn for a challenging hike.", 27.9950, 86.8283)
    ],
    "annapurna": [
        ("Tikhedhunga / Ulleri", "Begin the trek with a climb up thousands of stone steps.", 28.3517, 83.7431),
        ("Ghorepani", "Trek through dense rhododendron forests.", 28.4000, 83.6933),
        ("Poon Hill", "An early morning hike to Poon Hill.", 28.4011, 83.6894),
        ("Tadapani", "Descend through lush forests.", 28.3967, 83.7667),
        ("Chhomrong", "Cross suspension bridges over the Modi Khola.", 28.4194, 83.8219),
        ("Dovan / Bamboo", "Trek into the deeper gorge.", 28.4611, 83.8403),
        ("Machhapuchhre Base Camp (MBC)", "Trek past bamboo forests.", 28.5133, 83.8731),
        ("Annapurna Base Camp (ABC)", "Arrive at the sanctuary's heart.", 28.5300, 83.8780)
    ],
    "kathmandu": [
        ("Kathmandu Durbar Square", "Explore the ancient royal palace courtyards.", 27.7042, 85.3065),
        ("Swayambhunath", "Climb the steps to this iconic hilltop stupa.", 27.7149, 85.2899),
        ("Pashupatinath Temple", "Visit the most sacred Hindu temple.", 27.7104, 85.3487),
        ("Boudhanath Stupa", "Walk around one of the largest spherical stupas.", 27.7215, 85.3620),
        ("Patan Durbar Square", "Take a short drive to the city of fine arts.", 27.6727, 85.3253),
        ("Bhaktapur Durbar Square", "Step back in time in this preserved medieval city.", 27.6722, 85.4283)
    ],
    "mustang": [
        ("Kagbeni", "Enter the restricted region through this ancient village.", 28.8353, 83.7825),
        ("Chele", "Trek through dramatic arid landscapes.", 28.9100, 83.8183),
        ("Syangboche", "Climb steep ridges, passing by chortens.", 28.9667, 83.8417),
        ("Ghami", "Walk past the longest Mani wall in Mustang.", 29.0667, 83.8750),
        ("Tsarang", "Explore ancient monasteries.", 29.1111, 83.9722),
        ("Lo Manthang", "Arrive at the mystical walled capital.", 29.1822, 83.9575)
    ],
    "lumbini": [
        ("Sacred Garden & Maya Devi Temple", "Visit the exact birthplace of Lord Buddha.", 27.4786, 83.2759),
        ("Monastic Zone (East & West)", "Explore beautifully crafted monasteries.", 27.4878, 83.2751),
        ("World Peace Pagoda", "Take a peaceful stroll.", 27.4981, 83.2764)
    ],
    "rara": [
        ("Jumla & Sinja Valley", "Trek through historic trade routes.", 29.2747, 82.1838),
        ("Rara Lake", "Reach the stunning, deep blue Rara Lake.", 29.5311, 82.0805),
        ("Murma Top", "Hike up to Murma Top for a breathtaking view.", 29.5400, 82.0500)
    ],
    "ghandruk": [
        ("Nayapul", "Begin the journey.", 28.2970, 83.7744),
        ("Birethanti", "Register at the checkpost.", 28.3075, 83.7725),
        ("Syauli Bazaar", "Walk along the Modi river.", 28.3314, 83.7770),
        ("Kimche", "Uphill climb towards Ghandruk.", 28.3582, 83.8058),
        ("Ghandruk Village", "Explore the beautiful Gurung settlement.", 28.3753, 83.8048),
        ("Gurung Museum", "Learn about the local culture.", 28.3760, 83.8050)
    ]
}

TRANSITIONAL_ACTIVITIES = [
    ("En Route Scenic Trek", "Continue the journey along winding trails.", 0.005, 0.005),
    ("Village Discovery", "Pass through quaint settlements.", -0.002, 0.003),
    ("River Crossing & Valley Walk", "Navigate across suspension bridges.", 0.003, -0.004),
    ("Uphill Ascent & Exploration", "A challenging yet rewarding day.", 0.006, 0.001),
    ("Descent Through Forests", "Enjoy a relaxing downhill walk.", -0.005, -0.002)
]

def get_spots_for_destination(dest_name, title):
    name_lower = dest_name.lower()
    title_lower = title.lower()
    
    if 'everest' in title_lower or 'everest' in name_lower: return DESTINATION_KNOWLEDGE['everest']
    if 'annapurna' in title_lower or 'annapurna' in name_lower or 'poon' in title_lower or 'poon' in name_lower: return DESTINATION_KNOWLEDGE['annapurna']
    if 'ghandruk' in title_lower or 'ghandruk' in name_lower: return DESTINATION_KNOWLEDGE['ghandruk']
    if 'pokhara' in title_lower or 'pokhara' in name_lower: return DESTINATION_KNOWLEDGE['pokhara']
    if 'chitwan' in title_lower or 'chitwan' in name_lower or 'bardia' in title_lower or 'bardia' in name_lower: return DESTINATION_KNOWLEDGE['chitwan']
    if 'kathmandu' in title_lower or 'kathmandu' in name_lower: return DESTINATION_KNOWLEDGE['kathmandu']
    if 'mustang' in title_lower or 'mustang' in name_lower: return DESTINATION_KNOWLEDGE['mustang']
    if 'lumbini' in title_lower or 'lumbini' in name_lower: return DESTINATION_KNOWLEDGE['lumbini']
    if 'rara' in title_lower or 'rara' in name_lower: return DESTINATION_KNOWLEDGE['rara']
    
    # Generic generic center coordinates for fallback
    return [
        ("Local Village Exploration", "Walk through traditional settlements.", 27.7172, 85.3240),
        ("Scenic Viewpoint Hike", "Hike up to a prominent hill or ridge.", 27.7272, 85.3340),
        ("Cultural Heritage Site", "Visit an ancient temple, monastery, or historical ruin.", 27.7072, 85.3140)
    ]

def generate_day_details(day, duration, title, destination):
    spots = get_spots_for_destination(destination, title)
    is_trek = 'trek' in title.lower() or 'base camp' in title.lower() or 'circuit' in title.lower() or 'poon' in title.lower()
    
    # We need to return (title, desc, lat, lng)
    # Default/central coord for the start/end
    start_lat, start_lng = spots[0][2], spots[0][3]
    end_lat, end_lng = spots[-1][2], spots[-1][3]
    
    if duration == 1:
        spot_names = ", ".join([s[0] for s in spots[:3]])
        return (f"Full Day {destination} Tour", f"Explore the highlights of {destination}, including {spot_names}.", start_lat, start_lng)
            
    intermediate_days = duration
    day_index = day - 1 
    
    if is_trek and duration >= 10 and day == 5:
        float_idx = (day_index / (duration - 1)) * (len(spots) - 1)
        lower_idx = int(float_idx)
        return ("Acclimatization and Rest Day", "Today is dedicated to acclimatization. We will take a short hike.", spots[lower_idx][2] + 0.001, spots[lower_idx][3] + 0.001)

    # Linearly interpolate day_index over spots array
    if duration <= 1:
        float_idx = 0
    else:
        float_idx = (day_index / (duration - 1)) * (len(spots) - 1)
        
    lower_idx = int(float_idx)
    upper_idx = min(len(spots) - 1, lower_idx + 1)
    fraction = float_idx - lower_idx
    
    if lower_idx == upper_idx:
        assigned_spot = spots[lower_idx]
        lat, lng = assigned_spot[2], assigned_spot[3]
        spot_name, spot_desc = assigned_spot[0], assigned_spot[1]
    else:
        spot_A = spots[lower_idx]
        spot_B = spots[upper_idx]
        lat = spot_A[2] + (spot_B[2] - spot_A[2]) * fraction
        lng = spot_A[3] + (spot_B[3] - spot_A[3]) * fraction
        spot_name, spot_desc = spot_B[0], spot_B[1]
        
    if is_trek:
        return (f"Trek to {spot_name}", f"Today's trail takes us towards {spot_name}. {spot_desc}", lat, lng)
    else:
        return (f"Exploring {spot_name}", f"Today is dedicated to exploring {spot_name}. {spot_desc}", lat, lng)

def update_itineraries():
    conn = db.get_db_connection()
    cursor = conn.cursor()
    
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
            day_title, day_desc, lat, lng = generate_day_details(day, duration, title, destination)
            itineraries_to_insert.append((pkg_id, day, day_title, day_desc, lat, lng))
            
    if itineraries_to_insert:
        cursor.executemany(
            "INSERT INTO package_itineraries (package_id, day_number, title, description, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s)",
            itineraries_to_insert
        )
        conn.commit()
        print(f"Updated {len(itineraries_to_insert)} mapped itinerary days for {len(packages)} packages.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_itineraries()
