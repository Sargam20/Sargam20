import urllib.request
import time
import random

url = "https://komarev.com/ghpvc/?username=Sargam20&style=for-the-badge&color=blue"

print("Starting FAST bumper!")
for i in range(1500):
    try:
        ping_url = f"{url}&_cb={random.randint(1000, 999999)}"
        # Add random user-agent to slightly obfuscate
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Mozilla/5.0 (X11; Linux x86_64)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)',
            'Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X)'
        ]
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        req = urllib.request.Request(ping_url, headers=headers)
        urllib.request.urlopen(req, timeout=5)
        print(f"Fast Ping {i+1} successful")
    except Exception as e:
        print(f"Fast Ping {i+1} failed: {e}")
    
    # Tiny delay to allow the server to breathe but still fast enough for 200/min
    time.sleep(0.1)

print("Finished fast bumping!")
