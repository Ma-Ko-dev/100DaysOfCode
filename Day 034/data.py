import requests

TRIVIA_URL = "https://opentdb.com/api.php"
PAYLOAD = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(TRIVIA_URL, params=PAYLOAD)
response.raise_for_status()
question_data = response.json()["results"]
