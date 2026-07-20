import os
import shutil
import random
from db import get_db_connection

# Define the source images
brain_dir = r"C:\Users\Acer\.gemini\antigravity-ide\brain\510998cf-5ee4-4e3b-9838-9b0da1831484"
static_img_dir = "static/images"

image_mappings = {
    "Mustang": ("mustang_nepal_1783572398517.png", "mustang_dest.png"),
    "Ghandruk": ("ghandruk_nepal_1783572420848.png", "ghandruk_dest.png"),
    "Langtang": ("langtang_nepal_1783572432797.png", "langtang_dest.png"),
    "Poon Hill": ("poonhill_nepal_1783572446454.png", "poonhill_dest.png"),
    "Ilam": ("ilam_nepal_1783572464981.png", "ilam_dest.png"),
    "Janakpur": ("janakpur_nepal_1783572476075.png", "janakpur_dest.png"),
    "Manaslu": (None, "annapurna_dest.png"), # Fallback to existing
    "Bandipur": (None, "kathmandu.jpg"), # Fallback to existing
    "Gosainkunda": (None, "rara_dest.png"), # Fallback to existing
    "Muktinath": ("mustang_nepal_1783572398517.png", "muktinath_dest.png") # Fallback to mustang
}

# Copy images to static directory
for dest_name, (src_name, dest_name_img) in image_mappings.items():
    if src_name:
        src_path = os.path.join(brain_dir, src_name)
        dest_path = os.path.join(static_img_dir, dest_name_img)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Copied {src_name} to {dest_name_img}")
        else:
            print(f"Source image {src_path} not found.")

# Data to insert
destinations_data = [
    ("Mustang", "Mustang District", "A remote and mystical kingdom with arid landscapes, ancient caves, and Tibetan culture.", "mustang_dest.png", "Mountain"),
    ("Ghandruk", "Kaski", "A beautiful Gurung village offering stunning views of the Annapurna and Machapuchare mountains.", "ghandruk_dest.png", "Heritage"),
    ("Langtang", "Rasuwa", "A spectacular valley known as the 'valley of glaciers' with rich Tamang culture.", "langtang_dest.png", "Mountain"),
    ("Poon Hill", "Myagdi", "Famous for its breathtaking sunrise views over the Annapurna and Dhaulagiri mountain ranges.", "poonhill_dest.png", "Mountain"),
    ("Ilam", "Ilam District", "Famous for its lush tea gardens, rolling hills, and pleasant climate.", "ilam_dest.png", "Nature"), # We can use Lake/Mountain/Heritage etc. Nature is not in the original categories, but it works. Let's use 'Mountain' or 'Heritage' or 'Lake' or 'Wildlife' or 'Adventure' for better insights grouping. I'll use 'Adventure' or just stick to the original categories. Let's map to existing categories: Mountain, Heritage, Lake, Wildlife, Adventure.
]

# Correcting categories to match existing insights categories (Mountain, Heritage, Lake, Wildlife, Adventure)
destinations_data = [
    ("Mustang", "Mustang District", "A remote and mystical kingdom with arid landscapes, ancient caves, and Tibetan culture.", "mustang_dest.png", "Mountain"),
    ("Ghandruk", "Kaski", "A beautiful Gurung village offering stunning views of the Annapurna and Machapuchare mountains.", "ghandruk_dest.png", "Heritage"),
    ("Langtang", "Rasuwa", "A spectacular valley known as the 'valley of glaciers' with rich Tamang culture.", "langtang_dest.png", "Mountain"),
    ("Poon Hill", "Myagdi", "Famous for its breathtaking sunrise views over the Annapurna and Dhaulagiri mountain ranges.", "poonhill_dest.png", "Mountain"),
    ("Ilam", "Ilam District", "Famous for its lush tea gardens, rolling hills, and pleasant climate.", "ilam_dest.png", "Adventure"),
    ("Janakpur", "Dhanusha", "The birthplace of Goddess Sita, famous for the grand Janaki Temple and Mithila culture.", "janakpur_dest.png", "Heritage"),
    ("Manaslu", "Gorkha", "A remote and challenging trekking destination offering pristine natural beauty.", "annapurna_dest.png", "Mountain"),
    ("Bandipur", "Tanahun", "A beautifully preserved Newari town with traditional architecture and mountain views.", "kathmandu.jpg", "Heritage"),
    ("Gosainkunda", "Rasuwa", "A sacred alpine freshwater lake situated at a high altitude.", "rara_dest.png", "Lake"),
    ("Muktinath", "Mustang", "A sacred pilgrimage site for both Hindus and Buddhists in the Himalayas.", "muktinath_dest.png", "Heritage")
]

packages_data = [
    # (Title, Description, Price, Duration, Max People, Image) - We'll append destination_id later
    ("Upper Mustang Trek - 14 Days", "Explore the hidden kingdom of Mustang and its ancient Tibetan culture.", 85000.00, 14, 10, "mustang_dest.png"),
    ("Ghandruk Village Tour - 3 Days", "Experience Gurung culture and stunning Annapurna views on a short trek.", 12000.00, 3, 15, "ghandruk_dest.png"),
    ("Langtang Valley Trek - 8 Days", "Trek through lush forests and glaciers in the beautiful Langtang valley.", 45000.00, 8, 12, "langtang_dest.png"),
    ("Poon Hill Sunrise Trek - 5 Days", "Enjoy the best sunrise views in the Himalayas on this classic short trek.", 25000.00, 5, 12, "poonhill_dest.png"),
    ("Ilam Tea Garden Tour - 4 Days", "Relax in the serene tea gardens of Ilam and enjoy the cool weather.", 18000.00, 4, 20, "ilam_dest.png"),
    ("Janakpur Cultural Tour - 2 Days", "Visit the holy Janaki Temple and explore the rich Mithila art and culture.", 10000.00, 2, 20, "janakpur_dest.png"),
    ("Manaslu Circuit Trek - 16 Days", "A challenging off-the-beaten-path trek around the stunning Mt. Manaslu.", 95000.00, 16, 8, "annapurna_dest.png"),
    ("Bandipur Heritage Stay - 2 Days", "Experience traditional Newari hospitality in the picturesque town of Bandipur.", 8000.00, 2, 10, "kathmandu.jpg"),
    ("Gosainkunda Lake Trek - 6 Days", "A spiritual journey to the sacred alpine lake of Gosainkunda.", 32000.00, 6, 12, "rara_dest.png"),
    ("Muktinath Pilgrimage Tour - 5 Days", "A holy trip to Muktinath by jeep or flight via Jomsom.", 38000.00, 5, 15, "muktinath_dest.png")
]

conn = get_db_connection()
cursor = conn.cursor()

# Insert destinations and collect their IDs
for i, dest in enumerate(destinations_data):
    cursor.execute(
        "INSERT INTO destinations (name, location, description, image, category) VALUES (%s, %s, %s, %s, %s)",
        dest
    )
    dest_id = cursor.lastrowid
    
    # Insert corresponding package
    pkg = packages_data[i]
    cursor.execute(
        "INSERT INTO packages (destination_id, title, description, price, duration_days, max_people, image) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (dest_id, pkg[0], pkg[1], pkg[2], pkg[3], pkg[4], pkg[5])
    )

conn.commit()
cursor.close()
conn.close()

print("Successfully added 10 popular destinations and packages with prices and matching figures.")
