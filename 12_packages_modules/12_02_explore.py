'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''
import requests
r=requests.get("http://api.spotify.com")
r.status_code

print(r.headers)
print(r.encoding)


import random
# generate a random number from the range 1-100
print(random.randint(1, 100))