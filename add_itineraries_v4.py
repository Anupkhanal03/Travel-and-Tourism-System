import db
import random

# Knowledge base of spots and activities for popular Nepal destinations
DESTINATION_KNOWLEDGE = {
    "pokhara": [
        ("Sarangkot", "Watch a breathtaking sunrise over the Annapurna and Dhaulagiri mountain ranges."),
        ("Fewa Lake", "Enjoy a peaceful boat ride and visit the Tal Barahi Temple situated on an island in the lake."),
        ("World Peace Pagoda", "Hike up to the Shanti Stupa for panoramic views of the Pokhara valley and the lake."),
        ("Davis Falls & Gupteshwor Cave", "Witness the mysterious underground waterfall and explore the deep, sacred cave nearby."),
        ("Begnas Lake", "Take a day trip to the quieter, pristine Begnas Lake and enjoy local fish delicacies."),
        ("International Mountain Museum", "Learn about the history of mountaineering in Nepal and the lifestyle of mountain people.")
    ],
    "chitwan": [
        ("Rapti River", "Enjoy a serene canoe ride at dawn, spotting crocodiles and various species of exotic birds."),
        ("Deep Jungle (Core Area)", "Embark on a thrilling jeep safari to track the endangered one-horned rhinoceros and Royal Bengal Tiger."),
        ("Tharu Village", "Experience the rich culture of the indigenous Tharu people, capped off with a traditional stick dance in the evening."),
        ("Elephant Breeding Center", "Visit the center to see baby elephants and learn about conservation efforts in the park."),
        ("Bishazari Tal (20,000 Lakes)", "Explore this wetland area, famous for bird watching and spotting marsh crocodiles in a tranquil setting.")
    ],
    "everest": [
        ("Lukla & Phakding", "Experience a thrilling flight to Lukla, followed by a scenic trek down to the village of Phakding."),
        ("Namche Bazaar", "Hike up to Namche, the vibrant Sherpa capital. We will rest here for acclimatization and explore the local markets."),
        ("Tengboche Monastery", "Visit the largest gompa in the Khumbu region, offering spectacular views of Ama Dablam and Everest."),
        ("Dingboche", "Trek through alpine meadows to reach Dingboche, a picturesque village surrounded by stone walls to protect crops."),
        ("Lobuche", "Navigate the rugged glacial moraines as we approach the final settlements before Base Camp."),
        ("Gorakshep", "Arrive at the last outpost before the Base Camp, preparing for the final push."),
        ("Everest Base Camp", "Reach the legendary Base Camp! Stand at the foot of the world's highest peak and celebrate your achievement."),
        ("Kala Patthar", "Wake up before dawn for a challenging hike to Kala Patthar to witness the ultimate golden sunrise over Mount Everest.")
    ],
    "annapurna": [
        ("Tikhedhunga / Ulleri", "Begin the trek with a climb up thousands of stone steps, surrounded by beautiful terraced farms."),
        ("Ghorepani", "Trek through dense rhododendron forests to reach Ghorepani, preparing for tomorrow's early morning hike."),
        ("Poon Hill", "An early morning hike to Poon Hill for one of the most famous sunrise views over the Annapurna and Dhaulagiri ranges."),
        ("Tadapani", "Descend through lush forests with occasional glimpses of langur monkeys and exotic birds."),
        ("Chhomrong", "Cross suspension bridges over the Modi Khola before climbing up to the beautiful Gurung village of Chhomrong."),
        ("Dovan / Bamboo", "Trek into the deeper gorge, surrounded by thick bamboo and oak forests."),
        ("Machhapuchhre Base Camp (MBC)", "Trek past bamboo forests and enter the sanctuary, enjoying close-up views of the Fishtail mountain."),
        ("Annapurna Base Camp (ABC)", "Arrive at the sanctuary's heart. Surrounded by 360-degree views of towering peaks, the sunset here is magical.")
    ],
    "kathmandu": [
        ("Kathmandu Durbar Square", "Explore the ancient royal palace courtyards, temples, and the residence of the living goddess, Kumari."),
        ("Swayambhunath (Monkey Temple)", "Climb the steps to this iconic hilltop stupa for a sweeping panoramic view of the Kathmandu Valley."),
        ("Pashupatinath Temple", "Visit the most sacred Hindu temple in Nepal, located on the banks of the Bagmati River, observing evening aarti."),
        ("Boudhanath Stupa", "Walk around one of the largest spherical stupas in the world, spinning prayer wheels alongside Tibetan monks."),
        ("Patan Durbar Square", "Take a short drive to the city of fine arts. Marvel at the intricate wood carvings and the stunning Krishna Mandir."),
        ("Bhaktapur Durbar Square", "Step back in time in this preserved medieval city, famous for pottery, the 55-Window Palace, and Nyatapola Temple.")
    ],
    "mustang": [
        ("Kagbeni", "Enter the restricted region through this ancient, fortress-like village located in the valley of the Kali Gandaki River."),
        ("Chele", "Trek through dramatic arid landscapes and canyon-like paths, crossing rivers and observing the unique geological formations."),
        ("Syangboche", "Climb steep ridges, passing by chortens and enjoying the expansive, wind-swept views of the high altitude desert."),
        ("Ghami", "Walk past the longest Mani wall in Mustang, surrounded by striking red cliffs."),
        ("Tsarang", "Explore ancient monasteries and the royal palace ruins in this historically rich village."),
        ("Lo Manthang", "Arrive at the mystical walled capital of Upper Mustang. Spend the day exploring the King's palace and ancient gompas.")
    ],
    "lumbini": [
        ("Sacred Garden & Maya Devi Temple", "Visit the exact birthplace of Lord Buddha and meditate under the ancient Bodhi tree near the sacred pond."),
        ("Monastic Zone (East & West)", "Explore beautifully crafted monasteries built by countries from all over the world, showcasing unique architectural styles."),
        ("World Peace Pagoda", "Take a peaceful stroll or a boat ride to the gleaming white Japanese Peace Pagoda at the edge of Lumbini.")
    ],
    "rara": [
        ("Jumla & Sinja Valley", "Trek through historic trade routes and the ancient Sinja Valley, the birthplace of the Nepali language."),
        ("Rara Lake", "Reach the stunning, deep blue Rara Lake, the largest in Nepal. Walk along its shores and enjoy the pristine alpine environment."),
        ("Murma Top", "Hike up to Murma Top for a breathtaking bird's-eye view of the entire lake and the surrounding snow-capped peaks.")
    ]
}

# Transitional activities when we have more days than key spots
TRANSITIONAL_ACTIVITIES = [
    ("En Route Scenic Trek", "Continue the journey along winding trails, enjoying the changing landscapes and connecting with fellow trekkers."),
    ("Village Discovery", "Pass through quaint settlements, taking time to observe local farming practices and traditional lifestyles."),
    ("River Crossing & Valley Walk", "Navigate across suspension bridges and follow the river valley, accompanied by the soothing sound of flowing water."),
    ("Uphill Ascent & Exploration", "A challenging yet rewarding day of gradual ascent, offering increasingly spectacular views of the snow-capped peaks."),
    ("Descent Through Forests", "Enjoy a relaxing downhill walk through lush forests, keeping an eye out for local wildlife and vibrant flora.")
]

def get_spots_for_destination(dest_name, title):
    name_lower = dest_name.lower()
    title_lower = title.lower()
    
    if 'everest' in title_lower or 'everest' in name_lower: return DESTINATION_KNOWLEDGE['everest']
    if 'annapurna' in title_lower or 'annapurna' in name_lower or 'poon' in title_lower or 'poon' in name_lower: return DESTINATION_KNOWLEDGE['annapurna']
    if 'pokhara' in title_lower or 'pokhara' in name_lower or 'ghandruk' in title_lower: return DESTINATION_KNOWLEDGE['pokhara']
    if 'chitwan' in title_lower or 'chitwan' in name_lower or 'bardia' in title_lower or 'bardia' in name_lower: return DESTINATION_KNOWLEDGE['chitwan']
    if 'kathmandu' in title_lower or 'kathmandu' in name_lower: return DESTINATION_KNOWLEDGE['kathmandu']
    if 'mustang' in title_lower or 'mustang' in name_lower: return DESTINATION_KNOWLEDGE['mustang']
    if 'lumbini' in title_lower or 'lumbini' in name_lower: return DESTINATION_KNOWLEDGE['lumbini']
    if 'rara' in title_lower or 'rara' in name_lower: return DESTINATION_KNOWLEDGE['rara']
    
    return [
        ("Local Village Exploration", "Walk through traditional settlements, observing local architecture and interacting with friendly locals."),
        ("Scenic Viewpoint Hike", "Hike up to a prominent hill or ridge to get a panoramic view of the surrounding landscapes and mountains."),
        ("Cultural Heritage Site", "Visit an ancient temple, monastery, or historical ruin to learn about the spiritual and cultural history of the region.")
    ]

def generate_day_details(day, duration, title, destination):
    spots = get_spots_for_destination(destination, title)
    is_trek = 'trek' in title.lower() or 'base camp' in title.lower() or 'circuit' in title.lower() or 'poon' in title.lower()
    
    if duration == 1:
        spot_names = ", ".join([s[0] for s in spots[:3]])
        return (f"Full Day {destination} Tour", f"Explore the highlights of {destination}, including {spot_names}. It will be a packed, memorable day!")
    
    if day == 1:
        return (f"Arrival in {destination} & Preparation", f"Welcome to your {title}! Upon arrival, you'll be greeted and transferred to your accommodation. Later, you might have time for a short stroll around the local area.")
            
    if day == duration:
        return ("Final Departure or Onward Journey", f"After a final hearty breakfast in {destination}, it's time to say goodbye! Take home unforgettable memories!")
            
    # Number of days available for activities
    intermediate_days = duration - 2 
    day_index = day - 2 # 0 to intermediate_days - 1
    
    if is_trek and duration >= 10 and day == 5:
        return ("Acclimatization and Rest Day", "To ensure a safe journey, today is dedicated to acclimatization. We will take a short hike to a higher viewpoint and then rest.")

    # We need to map `intermediate_days` to `len(spots)`.
    # If intermediate_days > len(spots), we inject transitional days.
    
    # We create a specific plan for the package duration by spreading the `spots` out.
    # To avoid repeating the exact same spot, we'll keep track of which spots are used on which day.
    
    # Let's dynamically build the itinerary for the whole trip the first time it's called (or just compute deterministically).
    # Since we need to be deterministic for this specific `day`, we will calculate the assigned spot.
    
    # If we have more days than spots, we insert transitional activities in between.
    assigned_spot = None
    transitional_activity = None
    
    if intermediate_days <= len(spots):
        # We have enough spots for all days (or more spots than days)
        spot_index = int((day_index / intermediate_days) * len(spots))
        assigned_spot = spots[spot_index]
    else:
        # We have more days than spots. We must pad with transitional activities.
        # How many padding days do we need?
        padding_needed = intermediate_days - len(spots)
        
        # We'll interleave spots and padding.
        # A simple deterministic way:
        # For every `day_index`, is it a "spot day" or a "padding day"?
        # We distribute the `len(spots)` evenly across `intermediate_days`.
        
        # Calculate ideal positions for the spots
        spot_positions = [int(i * (intermediate_days - 1) / max(1, len(spots) - 1)) for i in range(len(spots))]
        
        if day_index in spot_positions:
            spot_idx = spot_positions.index(day_index)
            assigned_spot = spots[spot_idx]
        else:
            trans_idx = day_index % len(TRANSITIONAL_ACTIVITIES)
            transitional_activity = TRANSITIONAL_ACTIVITIES[trans_idx]
            
    if assigned_spot:
        spot_name, spot_desc = assigned_spot
        if is_trek:
            return (f"Trek to {spot_name}", f"Today's trail takes us towards {spot_name}. {spot_desc} The trek will feature varying landscapes, and we'll take plenty of breaks to appreciate the stunning natural beauty.")
        else:
            return (f"Exploring {spot_name}", f"Today is dedicated to exploring {spot_name}. {spot_desc} Our guide will provide fascinating insights, and you'll have plenty of time for photography.")
    elif transitional_activity:
        trans_name, trans_desc = transitional_activity
        if is_trek:
            return (trans_name, trans_desc + " We will cover a good distance today at a steady pace, taking in the grand scale of the Himalayas.")
        else:
            return ("Leisure & Exploration Day", "Today is a more relaxed day. We will explore lesser-known areas, interact with locals, and enjoy the serene environment at our own pace.")
    
    # Fallback
    return ("Exploration Day", "We will continue our amazing journey today.")

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
            day_title, day_desc = generate_day_details(day, duration, title, destination)
            itineraries_to_insert.append((pkg_id, day, day_title, day_desc))
            
    if itineraries_to_insert:
        cursor.executemany(
            "INSERT INTO package_itineraries (package_id, day_number, title, description) VALUES (%s, %s, %s, %s)",
            itineraries_to_insert
        )
        conn.commit()
        print(f"Updated {len(itineraries_to_insert)} perfectly sequenced itinerary days for {len(packages)} packages.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_itineraries()
