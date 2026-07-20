from recommender import get_content_based_recommendations
from chatbot import chatbot_agent

print("=== Testing Recommender for Deepa (user_id=2) ===")
recs = get_content_based_recommendations(2, limit=3)
print(f"Recommendations returned: {len(recs)}")
for r in recs:
    print(f"  - {r['title']} | {r['match_score']}% match | {r['image']}")

print()
print("=== Testing Chatbot ===")
tests = [
    ("Tell me about Pokhara", None),
    ("What is the Everest Base Camp Trek?", None),
    ("Suggest wildlife packages", None),
    ("Packages under 20000", None),
    ("What are my bookings?", 2),
    ("Hello", None),
]
for query, uid in tests:
    resp = chatbot_agent.get_response(query, user_id=uid)
    print(f"Q: {query}")
    print(f"Intent: {resp['intent']}, Packages: {len(resp['packages'])}")
    print(f"Response (first 120 chars): {resp['response'][:120]}")
    print()
