import urllib.request
import os

images = {
    'hero': 'https://loremflickr.com/800/800/shoes?lock=100',
    'casual1': 'https://loremflickr.com/400/400/sneakers?lock=1',
    'casual2': 'https://loremflickr.com/400/400/sneakers?lock=2',
    'casual3': 'https://loremflickr.com/400/400/sneakers?lock=3',
    'formal1': 'https://loremflickr.com/400/400/leather_shoes?lock=4',
    'formal2': 'https://loremflickr.com/400/400/heels?lock=5',
    'formal3': 'https://loremflickr.com/400/400/loafers?lock=6',
    'formal4': 'https://loremflickr.com/400/400/boots?lock=7',
    'outdoor1': 'https://loremflickr.com/400/400/hiking_shoes?lock=8',
    'outdoor2': 'https://loremflickr.com/400/400/rain_boots?lock=9',
    'outdoor3': 'https://loremflickr.com/400/400/trail_running_shoes?lock=10',
    'home1': 'https://loremflickr.com/400/400/slippers?lock=11',
    'home2': 'https://loremflickr.com/400/400/sandals?lock=12',
    'home3': 'https://loremflickr.com/400/400/flip_flops?lock=13',
    'acc1': 'https://loremflickr.com/400/400/socks?lock=14',
    'acc2': 'https://loremflickr.com/400/400/insoles?lock=15',
    'acc3': 'https://loremflickr.com/400/400/shoelaces?lock=16',
    'product_main': 'https://loremflickr.com/800/600/shoes?lock=17'
}

os.makedirs('images', exist_ok=True)

for name, url in images.items():
    try:
        urllib.request.urlretrieve(url, f"images/{name}.jpg")
        print(f"Downloaded {name}.jpg")
    except Exception as e:
        print(f"Failed {name}: {e}")
