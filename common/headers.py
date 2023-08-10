import time
import hashlib

from helpers import dev_tools


class HEADER:
    HOST = "Host"
    USER_AGENT = "User-Agent"
    ACCEPT = "Accept"
    ACCEPT_LANGUAGE = "Accept-Language"
    ACCEPT_ENCODING = "Accept-Encoding"
    REFERER = "Referer"
    X_TZ_OFFSET = "X-tz-offset"
    DNT = "DNT"
    SEC_FETCH_DEST = "Sec-Fetch-Dest"
    SEC_FETCH_MODE = "Sec-Fetch-Mode"
    SEC_FETCH_SITE = "Sec-Fetch-Site"
    CONNECTION = "Connection"
    TIMESTAMP = "X-Ts"
    XPORT = "X-Port"
    COOKIE = "Cookie"
    XCSRFTOKEN = "X-CSRFToken"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_TYPE = "Content-Type"


class Header:
    def __init__(self) -> None:
        self.headers = {
            HEADER.HOST: "www.simcompanies.com",
            HEADER.USER_AGENT: "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
            HEADER.ACCEPT: "application/json, text/plain, */*",
            HEADER.ACCEPT_LANGUAGE: "en-US,en;q=0.5",
            HEADER.ACCEPT_ENCODING: "gzip, deflate, br",
            HEADER.REFERER: "https://www.simcompanies.com/",
            HEADER.X_TZ_OFFSET: "0",
            HEADER.DNT: "1",
            HEADER.SEC_FETCH_DEST: "empty",
            HEADER.SEC_FETCH_MODE: "cors",
            HEADER.SEC_FETCH_SITE: "same-origin",
            HEADER.CONNECTION: "keep-alive",
        }

    def json(self):
        return self.headers
    
    def update_timestamp(self, url=None, ts=None):
        if ts:
            self.headers[HEADER.TIMESTAMP] = ts
        else:
            self.headers[HEADER.TIMESTAMP] = str(int(time.time() * 1000))
        url_without_domain = url.replace("https://www.simcompanies.com", "")
        if url_without_domain[-1] != "/":
            url_without_domain += "/"
        input_data = f"{url_without_domain}{self.headers[HEADER.TIMESTAMP]}"
        self.headers[HEADER.XPORT] = hashlib.md5(input_data.encode('utf-8')).hexdigest()
        dev_tools.dev_print(self.headers)

    def update_cookies(self, cookies):
        self.headers[HEADER.COOKIE] = ""
        for cookie in cookies:
            self.headers[HEADER.COOKIE] += f"{cookie.name}={cookie.value}; "

            if cookie.name == "csrftoken":
                self.headers[HEADER.XCSRFTOKEN] = cookie.value
    
    # TODO: content length
    def update_content_length(self, content_length, content_type="application/json;charset=utf-8"):
        self.headers[HEADER.CONTENT_LENGTH] = content_length
        self.headers[HEADER.CONTENT_TYPE] = content_type
