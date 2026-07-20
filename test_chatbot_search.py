from chatbot import chatbot_agent
import re

def test_query(query, label):
    print("=" * 60)
    print(f"Testing {label}: '{query}'")
    print("=" * 60)
    try:
        res = chatbot_agent.get_response(query)
        print(f"Detected Intent: {res['intent']}")
        print(f"Local Packages Returned: {len(res['packages'])}")
        
        # Check if response contains web search results indicator
        has_search_results = "Web Search Results" in res['response']
        print(f"Contains Web Search Results: {has_search_results}")
        
        # Print snippet of response
        # To avoid console encoding issues on Windows, encode to ascii fallback
        clean_resp = re.sub(r'<[^>]+>', ' ', res['response'])
        clean_resp = ' '.join(clean_resp.split())
        safe_resp = clean_resp[:250] + "..." if len(clean_resp) > 250 else clean_resp
        safe_resp = safe_resp.encode('ascii', 'replace').decode('ascii')
        print(f"Clean Response: {safe_resp}\n")
    except Exception as e:
        print(f"Test failed with error: {e}\n")

if __name__ == "__main__":
    # Test Case 1: Local DB destination query (should NOT do web search)
    test_query("Tell me about Pokhara", "Local Destination Query")
    
    # Test Case 2: Explicit web search request (should do web search)
    test_query("search the web for Kathmandu weather", "Explicit Web Search")
    
    # Test Case 3: FAQ query (should do web search)
    test_query("Do I need a visa for Nepal?", "FAQ Query")
    
    # Test Case 4: General query/fallback (should do web search)
    test_query("who is the current prime minister of Nepal?", "General Query Fallback")
