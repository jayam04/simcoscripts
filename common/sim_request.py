import requests
from requests import Response

from common.headers import Headers
import json
import time


class Request:
    def __init__(self, url, body=None, headers=None, method="GET"):
        self.url = url
        self.body = body
        if headers:
            self.headers = headers
        else:
            self.headers = Headers()
        self.method = method

        if body:
            self.headers.set_content_length(len(body))
            self.headers.set_content_type()

    def __str__(self) -> str:
        return f"{self.url} {self.body} {self.headers}"


    def update_body(self, body: dict):
        self.body = json.dumps(body)
        self.headers.set_content_length(len(self.body))
        self.headers.set_content_type()

    def send(self) -> Response:
        if self.method == "GET":
            return requests.get(self.url, headers=self.headers.json())
        
        if self.method == "POST":
            return requests.post(self.url, data=self.body, headers=self.headers.json())

        if self.method == "PATCH":
            return requests.patch(self.url, data=self.body, headers=self.headers.json())
        
    def update_timestamp_and_xport(self, ts=None, url=None):
        if not ts:
            ts = int(time.time() * 1000)
        self.headers.set_timestamp(ts)

        if not url:
            url = self.url
        self.headers.set_xport(url)

    def update_cookies_and_csrftoken(self, cookies):
        self.headers.set_cookies_and_csrftoken(cookies)

