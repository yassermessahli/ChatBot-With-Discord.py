import requests
import json

def get_quote():
    response = requests.get('https://api.quotable.io/random')
    json_data = json.loads(response.text)
    return json_data['content']