import os
from db import get_db_connection

def update_schema_and_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Add new columns if they don't exist
    try:
        cursor.execute("ALTER TABLE destinations ADD COLUMN special_features TEXT")
        cursor.execute("ALTER TABLE destinations ADD COLUMN best_time_to_visit TEXT")
        cursor.execute("ALTER TABLE destinations ADD COLUMN history TEXT")
        print("Successfully added new columns to destinations table.")
    except Exception as e:
        print(f"Columns might already exist. Error: {e}")

    # 2. Data for the 19 destinations
    dest_data = {
        'Pokhara': (
            "Stunning views of the Annapurna range, Phewa Lake for boating, Paragliding from Sarangkot, and the Peace Pagoda.",
            "September to November and March to May for clear mountain views.",
            "Pokhara was an important point on the ancient trade route between Tibet and India. It was ruled by the Shah dynasty in the 18th century."
        ),
        'Chitwan National Park': (
            "One-horned rhinos, Bengal tigers, elephant back safaris, and Tharu culture.",
            "October to early March when temperatures are cooler and vegetation is less dense.",
            "Established in 1973, it is Nepal's first national park and a UNESCO World Heritage site since 1984, previously a royal hunting reserve."
        ),
        'Everest Base Camp': (
            "World's highest peak base camp, Sherpa culture, Tengboche Monastery, and Khumbu Icefall views.",
            "March to May and September to November.",
            "First successfully scaled by Sir Edmund Hillary and Tenzing Norgay in 1953, opening the region to modern trekking."
        ),
        'Kathmandu Durbar Square': (
            "Ancient temples, intricate wood carvings, Kumari Ghar (House of the Living Goddess), and Hanuman Dhoka Palace.",
            "All year round, though spring and autumn offer the most pleasant weather.",
            "The heart of ancient Kathmandu, it was the royal Nepalese residence until the 19th century and is a UNESCO World Heritage site."
        ),
        'Annapurna Conservation Area': (
            "Diverse flora and fauna, deep Kali Gandaki gorge, natural hot springs, and varied trekking routes.",
            "Autumn (Sept-Nov) and Spring (Mar-May).",
            "Established in 1986, it is Nepal's largest protected area and the first conservation area allowing local people to live within its boundaries."
        ),
        'Bardia National Park': (
            "High chance of seeing Royal Bengal Tigers, wild elephants, and Gangetic dolphins.",
            "Mid-September to mid-December and February to May.",
            "Originally a royal hunting reserve, it was gazetted as a national park in 1988 to preserve its pristine jungle ecosystem."
        ),
        'Lumbini': (
            "The Maya Devi Temple (birthplace of Buddha), Ashoka Pillar, and numerous international monasteries.",
            "October to March to avoid the intense summer heat.",
            "A UNESCO World Heritage site, it is the exact spot where Siddhartha Gautama (Lord Buddha) was born in 623 BC."
        ),
        'Rara Lake': (
            "Nepal's largest and deepest freshwater lake, surrounded by pine forests and snow-capped peaks.",
            "September, October, April, and May.",
            "Located in Rara National Park (established 1976), this pristine lake has remained largely untouched and remote."
        ),
        'Bhotekoshi River': (
            "Thrilling white-water rafting, extreme kayaking, and one of the world's highest bungee jumps.",
            "September to November and March to May.",
            "Flowing from the Himalayas in Tibet, it has carved steep gorges that have become Nepal's premier adventure sports destination."
        ),
        'Mustang': (
            "Arid desert landscapes, ancient cliff caves, Tibetan Buddhist culture, and the walled city of Lo Manthang.",
            "March to November (it lies in the rain shadow, making it good even during the monsoon).",
            "An ancient forbidden kingdom that was highly restricted to foreigners until 1992, preserving its unique Tibetan heritage."
        ),
        'Ghandruk': (
            "Traditional Gurung architecture, stone-paved alleys, and up-close views of Annapurna South and Machapuchare.",
            "September to November and March to May.",
            "A historically significant Gurung settlement that has served as a major recruitment center for the legendary Gurkha soldiers."
        ),
        'Langtang': (
            "Glaciers, alpine meadows, Yak pastures, and authentic Tamang villages.",
            "September to November and March to May.",
            "Nepal's first Himalayan national park (1976). It has a rich history tied to Tibetan traders who discovered the valley ('Lang' meaning yak, 'Tang' meaning to follow)."
        ),
        'Poon Hill': (
            "A spectacular panoramic sunrise view over the Annapurna and Dhaulagiri mountain ranges.",
            "September to November and March to May.",
            "Named after Tek Bahadur Pun, a pioneer who helped establish this viewpoint which is now one of the most famous short treks in the world."
        ),
        'Ilam': (
            "Lush rolling tea gardens, misty weather, Antu Danda sunrise, and Mai Pokhari.",
            "October to December and February to April.",
            "Nepal's tea-producing capital, deeply influenced by the tea-planting culture introduced in the 1860s."
        ),
        'Janakpur': (
            "The magnificent Janaki Mandir, vibrant Mithila art, and holy ponds like Dhanush Sagar.",
            "October to March.",
            "An ancient city mentioned in the Hindu epic Ramayana as the birthplace of Goddess Sita and the place where her marriage to Lord Rama occurred."
        ),
        'Manaslu': (
            "The eighth highest mountain in the world, remote Tibetan-influenced villages, and the challenging Larkya La pass.",
            "September to November and March to May.",
            "The region was officially opened to foreign trekkers only in 1991, preserving its pristine nature and ancient trading routes to Tibet."
        ),
        'Bandipur': (
            "Beautifully preserved 18th-century Newari architecture, no-vehicle main street, and mountain panoramas.",
            "September to November and March to May.",
            "Originally a simple Magar village, it transformed into a prosperous trading hub in the 19th century when Newari merchants moved in from the Kathmandu Valley."
        ),
        'Gosainkunda': (
            "A complex of 108 alpine oligotrophic lakes surrounded by rugged mountains.",
            "September to November and March to May. (Also during Janai Purnima in August for pilgrims).",
            "According to Hindu mythology, the lake was created by Lord Shiva with his trident (Trishul) to extract water to cool his burning throat after swallowing poison."
        ),
        'Muktinath': (
            "A sacred temple with 108 waterspouts, an eternal flame, and stark mountainous scenery.",
            "March to June and September to November.",
            "A highly venerated site for both Hindus and Buddhists, symbolizing liberation (Moksha) and the intertwining of two ancient faiths."
        )
    }

    # 3. Update the table
    for name, data in dest_data.items():
        cursor.execute("""
            UPDATE destinations 
            SET special_features = %s, best_time_to_visit = %s, history = %s 
            WHERE name = %s
        """, (data[0], data[1], data[2], name))
    
    conn.commit()
    print(f"Updated {len(dest_data)} destinations with specific information.")
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_schema_and_data()
