import urllib.request

# Authentic, realistic wildlife photography of a Bengal Tiger (Wikimedia Commons)
image_url = "https://upload.wikimedia.org/wikipedia/commons/1/17/Tiger_in_Ranthambhore.jpg"
image_path = "static/images/bardia_pkg.jpg"

try:
    req = urllib.request.Request(
        image_url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    with urllib.request.urlopen(req) as response, open(image_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print("Successfully replaced bardia_pkg.jpg with a highly realistic tiger photo.")
except Exception as e:
    print(f"Failed to download image: {e}")
