import requests

from common.headers import Header
import json

class Request:
    def __init__(self, url, body=None, headers=None, method="GET"):
        self.url = url
        self.body = body
        if headers:
            self.headers = headers
        else:
            self.headers = Header()
        self.method = method

        # TODO: what is len body > 0, update headers.content-length, type and more
        if body:
            headers.update_content_length(str(len(body)))

    def update_body(self, body):
        self.body = json.dumps(body)
        self.headers.update_content_length(str(len(self.body)))

    def send(self):
        if self.method == "GET":
            print(self.headers.json())
            return requests.get(self.url, headers=self.headers.json())
        
        if self.method == "POST":
            return requests.post(self.url, data=self.body, headers=self.headers.json())