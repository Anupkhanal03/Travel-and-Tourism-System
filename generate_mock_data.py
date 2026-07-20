import random
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from db import get_db_connection

def generate():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Insert some destinations if they don't exist
    additional_destinations = [
        ("Annapurna Conservation Area", "Kaski/Manang", "Home to the world-famous Annapurna trekking circuit.", "Mountain", "annapurna_dest.png"),
        ("Bardia National Park", "Bardia", "Deep forests of Western Nepal, famous for Bengal Tigers.", "Wildlife", "bardia_dest.png"),
        ("Lumbini", "Rupandehi", "The sacred birthplace of Lord Buddha, a world heritage site.", "Heritage", "lumbini_dest.png"),
        ("Rara Lake", "Mugu", "The largest and deepest freshwater lake in Nepal, a pristine jewel.", "Lake", "rara_dest.png"),
        ("Bhotekoshi River", "Sindhupalchok", "Known for white water rafting and high-adrenaline bungee jumping.", "Adventure", "bhotekoshi_dest.png")
    ]
    
    dest_ids = {}
    
    # Get existing destinations
    cursor.execute("SELECT id, name FROM destinations")
    existing_dests = {row['name']: row['id'] for row in cursor.fetchall()}
    
    for name, loc, desc, cat, img in additional_destinations:
        if name not in existing_dests:
            cursor.execute(
                "INSERT INTO destinations (name, location, description, image, category) VALUES (%s, %s, %s, %s, %s)",
                (name, loc, desc, img, cat)
            )
            dest_ids[name] = cursor.lastrowid
        else:
            dest_ids[name] = existing_dests[name]
            
    # Add original destinations to dest_ids map
    for name, did in existing_dests.items():
        dest_ids[name] = did
        
    conn.commit()

    # 2. Insert some packages if they don't exist
    additional_packages = [
        (dest_ids["Annapurna Conservation Area"], "Annapurna Base Camp Trek - 10 Days", "Experience the heart of the Annapurnas.", 55000.00, 10, 12, "annapurna_pkg.png"),
        (dest_ids["Bardia National Park"], "Bardia Tiger Encounter - 3 Days", "Track wild tigers in the pristine forests of Western Nepal.", 18000.00, 3, 8, "bardia_pkg.jpg"),
        (dest_ids["Lumbini"], "Buddhist Heritage Pilgrimage - 2 Days", "Visit the birthplace of Buddha and ancient monasteries.", 8500.00, 2, 15, "lumbini_pkg.png"),
        (dest_ids["Rara Lake"], "Rara Wilderness Tour - 6 Days", "A journey to the most remote and scenic lake in Nepal.", 35000.00, 6, 8, "rara_pkg.png"),
        (dest_ids["Bhotekoshi River"], "Bhotekoshi White Water Rafting & Bungee", "One day of extreme rafting and a giant bridge bungee jump.", 15000.00, 1, 10, "bhotekoshi_pkg.png")
    ]
    
    cursor.execute("SELECT id, title FROM packages")
    existing_packages = {row['title']: row['id'] for row in cursor.fetchall()}
    
    pkg_ids = []
    for dest_id, title, desc, price, duration, max_p, img in additional_packages:
        if title not in existing_packages:
            cursor.execute(
                "INSERT INTO packages (destination_id, title, description, price, duration_days, max_people, image) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (dest_id, title, desc, price, duration, max_p, img)
            )
            pkg_ids.append((cursor.lastrowid, price))
        else:
            pkg_ids.append((existing_packages[title], price))
            
    # Include original packages
    cursor.execute("SELECT id, title, price FROM packages")
    all_current_packages = cursor.fetchall()
    pkg_ids = [(row['id'], float(row['price'])) for row in all_current_packages]
    
    conn.commit()

    # 3. Create mock users
    mock_user_names = [
        "Rohan Shrestha", "Binita Thapa", "Sujan Adhikari", "Prativa Pandey", 
        "Aayush Shakya", "Sita Dahal", "Manish Gurung", "Kiran Basnet", 
        "Niranjan Karki", "Aarati Tamang"
    ]
    
    cursor.execute("SELECT id, email FROM users")
    existing_users = {row['email']: row['id'] for row in cursor.fetchall()}
    
    user_ids = list(existing_users.values())
    
    for name in mock_user_names:
        email = name.lower().replace(" ", "") + "@gmail.com"
        if email not in existing_users:
            pw_hash = generate_password_hash("password123")
            phone = "98" + "".join(random.choices("0123456789", k=8))
            cursor.execute(
                "INSERT INTO users (full_name, email, password, phone, role) VALUES (%s, %s, %s, %s, 'user')",
                (name, email, pw_hash, phone)
            )
            user_ids.append(cursor.lastrowid)
            
    conn.commit()
    
    # Filter out admin (ID 1 is admin 'Anup Khanal')
    user_ids = [uid for uid in user_ids if uid != 1]
    
    # 4. Generate ~120 bookings over the last 6 months (180 days)
    # Start date: 180 days ago
    start_date = datetime.now() - timedelta(days=180)
    
    payment_methods = ["eSewa", "Khalti", "Fonepay"]
    statuses = ["Confirmed", "Cancelled", "Pending"]
    status_weights = [0.75, 0.15, 0.10]
    
    count = 0
    for _ in range(120):
        # Pick random user and package
        user_id = random.choice(user_ids)
        package_id, price = random.choice(pkg_ids)
        
        # Pick random date in the last 180 days
        days_offset = random.randint(0, 180)
        booked_at = start_date + timedelta(days=days_offset, hours=random.randint(0, 23), minutes=random.randint(0, 59))
        
        # Travel date is usually 10 to 40 days after booked_at
        travel_date = (booked_at + timedelta(days=random.randint(10, 40))).date()
        
        num_people = random.randint(1, 4)
        total_price = price * num_people
        
        status = random.choices(statuses, weights=status_weights)[0]
        payment_method = random.choice(payment_methods)
        
        # Set payment status
        if status == "Confirmed":
            payment_status = "Paid"
            transaction_id = "TXN" + "".join(random.choices("0123456789QWERTYUIOP", k=10))
            paid_at = booked_at + timedelta(minutes=random.randint(2, 15))
        elif status == "Pending":
            # 50% paid, 50% unpaid
            payment_status = random.choice(["Paid", "Unpaid"])
            if payment_status == "Paid":
                transaction_id = "TXN" + "".join(random.choices("0123456789QWERTYUIOP", k=10))
                paid_at = booked_at + timedelta(minutes=random.randint(2, 15))
            else:
                transaction_id = None
                paid_at = None
        else: # Cancelled
            payment_status = random.choice(["Paid", "Unpaid"])
            transaction_id = "TXN" + "".join(random.choices("0123456789QWERTYUIOP", k=10)) if payment_status == "Paid" else None
            paid_at = booked_at + timedelta(minutes=random.randint(2, 15)) if payment_status == "Paid" else None
            
        cursor.execute("""
            INSERT INTO bookings (user_id, package_id, num_people, travel_date, total_price, status, payment_status, payment_method, transaction_id, paid_at, booked_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, package_id, num_people, travel_date, total_price, status, payment_status, payment_method, transaction_id, paid_at, booked_at))
        count += 1
        
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Successfully generated {count} mock bookings, additional packages, and users!")

if __name__ == '__main__':
    generate()
