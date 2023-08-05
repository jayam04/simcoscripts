class Header:
    def __init__(self) -> None:
        self.headers = {
            "Host": "www.simcompanies.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.simcompanies.com/",
            "X-tz-offset": "0",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
        }

    def json(self):
        return self.headers
    
    def update_timestamp(self, ts=None):
        # TODO: No timestamp
        self.headers["X-Ts"] = ts
        # TODO: xport

    def update_cookies(self, cookies):
        self.headers["Cookie"] = ""
        for cookie in cookies:
            self.headers["Cookie"] += f"{cookie.name}={cookie.value}; "

            if cookie.name == "csrftoken":
                self.headers["X-CSRFToken"] = cookie.value
    
    # TODO: content length
    def update_content_length(self, content_length, content_type="application/json;charset=utf-8"):
        self.headers["Content-Length"] = content_length
        self.headers["Content-Type"] = content_type