import requests

url = "http://127.0.0.1:8000/process-text/"

data = {
    "text": "Hello 😄   iLoveText 🚀",
    "remove_emoji": True,
    "remove_spaces": True
}
data = {
    "text": "She dont like apples and banana.",
    "grammar": True
}

response = requests.post(url, json=data)
print(response.json())
