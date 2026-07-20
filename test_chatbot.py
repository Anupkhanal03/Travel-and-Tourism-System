from chatbot import chatbot_agent

queries = [
    "Tell me about Rara Lake",
    "What is the Annapurna Base Camp Trek?",
    "my bookings"
]

for q in queries:
    print(f"--- Query: {q} ---")
    resp = chatbot_agent.get_response(q, user_id=1)
    print("Intent:", resp['intent'])
    print("Response:", resp['response'])
    print()
