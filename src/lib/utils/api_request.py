import json
import requests


class ApiRequest:
    def get_json(url):
        result = requests.get(url)
        return json.loads(result.text)
