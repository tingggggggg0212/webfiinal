import urllib.request
import json

url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrsearch=shoe%20product%20shot%20isolated&gsrlimit=20&prop=imageinfo&iiprop=url"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(html)
    for page in data['query']['pages'].values():
        print(page['imageinfo'][0]['url'])
except Exception as e:
    print("Error:", e)
