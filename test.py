import requests
import json

url = "http://localhost:9090/"

response = requests.request("GET", url, timeout=1)

data = json.loads(response.text)

assert(data["data"] == "hello")