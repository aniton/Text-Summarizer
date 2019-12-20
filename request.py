import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={ "original": 1,
        "summary": 1,
        "accuracy": 1,
        "ratio": 1})

print(r.json())