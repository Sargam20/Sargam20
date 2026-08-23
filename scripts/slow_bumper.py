import urllib.request
import time
import random

url = "https://komarev.com/ghpvc/?username=Sargam20&style=for-the-badge&color=blue"

# Ping up to 1500 times slowly to avoid spam detection
for i in range(1500):
    try:
        # Cache buster to ensure it's not cached locally or by proxies
        ping_url = f"{url}&_cb={random.randint(1000, 999999)}"
        req = urllib.request.Request(ping_url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req)
        print(f"Ping {i+1} successful")
    except Exception as e:
        print(f"Ping {i+1} failed: {e}")
    
    # Sleep 2 to 4 seconds between requests to look like human traffic
    time.sleep(random.uniform(2.0, 4.0))

print("Finished slow-pinging!")
