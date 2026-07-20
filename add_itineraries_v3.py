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
        ("Lobuche & Gorakshep", "Navigate the rugged glacial moraines as we approach the final settlements before Base Camp."),
        ("Everest Base Camp", "Reach the legendary Base Camp! Stand at the foot of the world's highest peak and celebrate your achievement."),
        ("Kala Patthar", "Wake up before dawn for a challenging hike to Kala Patthar to witness the ultimate golden sunrise over Mount Everest.")
    ],
    "annapurna": [
        ("Tikhedhunga / Ulleri", "Begin the trek with a climb up thousands of stone steps, surrounded by beautiful terraced farms."),
        ("Ghorepani", "Trek through dense rhododendron forests to reach Ghorepani, preparing for tomorrow's early morning hike."),
        ("Poon Hill", "An early morning hike to Poon Hill for one of the most famous sunrise views over the Annapurna and Dhaulagiri ranges."),
        ("Chhomrong", "Descend and cross suspension bridges over the Modi Khola before climbing up to the beautiful Gurung village of Chhomrong."),
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
        ("Ghami & Tsarang", "Walk past the longest Mani wall in Mustang, surrounded by striking red cliffs and ancient monasteries."),
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

def get_spots_for_destination(dest_name, title):
    name_lower = dest_name.lower()
    title_lower = title.lower()
    
    # Try to match based on keywords
    if 'everest' in title_lower or 'everest' in name_lower: return DESTINATION_KNOWLEDGE['everest']
    if 'annapurna' in title_lower or 'annapurna' in name_lower or 'poon' in title_lower or 'poon' in name_lower: return DESTINATION_KNOWLEDGE['annapurna']
    if 'pokhara' in title_lower or 'pokhara' in name_lower or 'ghandruk' in title_lower: return DESTINATION_KNOWLEDGE['pokhara']
    if 'chitwan' in title_lower or 'chitwan' in name_lower or 'bardia' in title_lower or 'bardia' in name_lower: return DESTINATION_KNOWLEDGE['chitwan']
    if 'kathmandu' in title_lower or 'kathmandu' in name_lower: return DESTINATION_KNOWLEDGE['kathmandu']
    if 'mustang' in title_lower or 'mustang' in name_lower: return DESTINATION_KNOWLEDGE['mustang']
    if 'lumbini' in title_lower or 'lumbini' in name_lower: return DESTINATION_KNOWLEDGE['lumbini']
    if 'rara' in title_lower or 'rara' in name_lower: return DESTINATION_KNOWLEDGE['rara']
    
    # Generic fallback
    return [
        ("Local Village Exploration", "Walk through traditional settlements, observing local architecture and interacting with friendly locals."),
        ("Scenic Viewpoint Hike", "Hike up to a prominent hill or ridge to get a panoramic view of the surrounding landscapes and mountains."),
        ("Cultural Heritage Site", "Visit an ancient temple, monastery, or historical ruin to learn about the spiritual and cultural history of the region."),
        ("Nature Trail Walk", "Enjoy a peaceful walk through forests or along riversides, taking in the flora and fauna of the area."),
        ("Local Market Visit", "Explore a bustling local market, taste regional delicacies, and maybe shop for some handmade souvenirs.")
    ]

def generate_day_details(day, duration, title, destination):
    spots = get_spots_for_destination(destination, title)
    is_trek = 'trek' in title.lower() or 'base camp' in title.lower() or 'circuit' in title.lower() or 'poon' in title.lower()
    
    # 1-day tours
    if duration == 1:
        spot_names = ", ".join([s[0] for s in spots[:3]])
        return (f"Full Day {destination} Tour", 
                f"Today we will explore the highlights of {destination}, including visits to {spot_names}. You will engage in activities like {spots[0][1].lower()} It will be a packed, memorable day!")
    
    # First Day
    if day == 1:
        return (f"Arrival in {destination} & Preparation", 
                f"Welcome to your {title}! Upon arrival, you'll be greeted and transferred to your accommodation. We'll have a brief orientation. Later, you might have time for a short stroll around the local area to soak in the atmosphere before the main adventure starts tomorrow.")
            
    # Last Day
    if day == duration:
        return ("Final Departure or Onward Journey", 
                f"After a final hearty breakfast in {destination}, it's time to say goodbye! You may have some free time for last-minute souvenir shopping before we arrange your transfer for departure. Take home unforgettable memories!")
            
    # Intermediate Days logic
    # We want to distribute the spots across the available intermediate days.
    intermediate_days = duration - 2
    if intermediate_days <= 0:
        intermediate_days = 1 # Safety fallback
        
    day_index = day - 2 # 0-indexed for intermediate days
    
    if is_trek and duration >= 10 and day == 5:
        return ("Acclimatization and Rest Day", 
                "To ensure a safe and enjoyable journey, today is dedicated to acclimatization. We will take a short hike to a higher viewpoint during the day, and then rest, letting our bodies adjust to the altitude.")

    # Select a spot based on the day progression
    # Map day_index (0 to intermediate_days-1) to spot_index (0 to len(spots)-1)
    spot_index = int((day_index / intermediate_days) * len(spots))
    if spot_index >= len(spots):
        spot_index = len(spots) - 1
        
    spot_name, spot_desc = spots[spot_index]
    
    if is_trek:
        return (f"Trek to {spot_name}", 
                f"Today's trail takes us towards {spot_name}. {spot_desc} The trek will feature varying landscapes, and we'll take plenty of breaks to appreciate the stunning natural beauty.")
    else:
        return (f"Exploring {spot_name}", 
                f"Today is dedicated to exploring {spot_name}. {spot_desc} Our guide will provide fascinating insights, and you'll have plenty of time for photography and soaking in the experience.")

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
        print(f"Updated {len(itineraries_to_insert)} hyper-specific itinerary days for {len(packages)} packages.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_itineraries()
