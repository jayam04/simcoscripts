import requests
from common.headers import Headers

class Request:
    def __init__(self, url, body=None, headers=Headers(), method="GET"):
        self.url = url
        self.body = body
        self.headers = headers
        self.method = method

        # TODO: what is len body > 0, update headers.content-length, type and more

    def send(self):
        if self.method == "GET":
            return requests.get(self.url, headers=self.headers)
        
        # TODO: add POST