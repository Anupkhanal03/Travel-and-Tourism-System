import requests, re, time

def test(msg, label):
    r = requests.post('http://127.0.0.1:5000/api/chat', json={'message': msg})
    data = r.json()
    clean = re.sub('<[^>]+>', ' ', data['response'])
    clean = ' '.join(clean.split())
    intent = data['intent']
    packages_count = len(data['packages'])
    has_web = 'Web Search Results' in data['response']
    safe = clean[:350].encode('ascii','replace').decode('ascii')
    print(f'=== {label} ===')
    print(f'  Intent: {intent}')
    print(f'  Packages: {packages_count}')
    print(f'  Web Search Results: {has_web}')
    print(f'  Response: {safe}')
    print()

test('Tell me about Everest', 'LOCAL - Destination query')
time.sleep(1)
test('search for best trekking routes in Nepal', 'EXPLICIT - Web search trigger')
time.sleep(1)
test('What currency is used in Nepal?', 'FAQ - Currency question')
