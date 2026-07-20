from db import get_db_connection
from recommender import get_content_based_recommendations

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT id FROM users WHERE email='deepa@gmail.com'")
user = cursor.fetchone()
if user:
    user_id = user['id']
    print(f"User ID for Deepa: {user_id}")
    recs = get_content_based_recommendations(user_id)
    print("Recommendations returned:", len(recs))
    for r in recs:
        print(f"- {r['title']}")
else:
    print("User not found!")
