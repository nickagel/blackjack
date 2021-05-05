from requests.sessions import should_bypass_proxies


import requests
import json


class ApiRequest:
    def get_json(url):
        result = requests.get(url)
        return json.loads(result.text)
