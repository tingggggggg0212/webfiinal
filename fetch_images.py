import urllib.request
import re

url = "https://unsplash.com/s/photos/shoe-product"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find image URLs like https://images.unsplash.com/photo-...
    photos = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
    # Deduplicate and print
    photos = list(set(photos))
    for p in photos[:16]:
        print(p + "?auto=format&fit=crop&w=800&q=80")
except Exception as e:
    print("Error:", e)
