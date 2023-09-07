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
    ORIGIN = "Origin"
    XCSRFTOKEN = "X-CSRFToken"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_TYPE = "Content-Type"


class Headers:
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
        self.HOST = "www.simcompanies.com"
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"
        self.ACCEPT = "application/json, text/plain, */*"
        self.ACCEPT_LANGUAGE = "en-US,en;q=0.5"
        self.ACCEPT_ENCODING = "gzip, deflate, br"
        self.REFERER = "https://www.simcompanies.com/"
        self.X_TZ_OFFSET = "0"
        self.DNT = "1"
        self.SEC_FETCH_DEST = "empty"
        self.SEC_FETCH_MODE = "cors"
        self.SEC_FETCH_SITE = "same-origin"
        self.CONNECTION = "keep-alive"
        self.TIMESTAMP = None
        self.XPORT = None
        self.COOKIE = None
        self.XCSRFTOKEN = None
        self.CONTENT_LENGTH = None
        self.CONTENT_TYPE = None
        self.ORIGIN = None

    def json_from_header(self):
        return self.headers
    
    def __str__(self) -> str:
        json_obj = self.json()
        del json_obj[HEADER.COOKIE]
        del json_obj[HEADER.XCSRFTOKEN]
        return str(json_obj)

    def json(self):
        raw_json = {
            HEADER.HOST: self.HOST,
            HEADER.USER_AGENT: self.USER_AGENT,
            HEADER.ACCEPT: self.ACCEPT,
            HEADER.ACCEPT_LANGUAGE: self.ACCEPT_LANGUAGE,
            HEADER.ACCEPT_ENCODING: self.ACCEPT_ENCODING,
            HEADER.REFERER: self.REFERER,
            HEADER.X_TZ_OFFSET: self.X_TZ_OFFSET,
            HEADER.DNT: self.DNT,
            HEADER.SEC_FETCH_DEST: self.SEC_FETCH_DEST,
            HEADER.SEC_FETCH_MODE: self.SEC_FETCH_MODE,
            HEADER.SEC_FETCH_SITE: self.SEC_FETCH_SITE,
            HEADER.CONNECTION: self.CONNECTION,
            HEADER.TIMESTAMP: self.TIMESTAMP,
            HEADER.XPORT: self.XPORT,
            HEADER.COOKIE: self.COOKIE,
            HEADER.XCSRFTOKEN: self.XCSRFTOKEN,
            HEADER.CONTENT_LENGTH: self.CONTENT_LENGTH,
            HEADER.CONTENT_TYPE: self.CONTENT_TYPE
        }

        keys_to_delete = [key for key, value in raw_json.items() if value is None]
        for key in keys_to_delete:
            del raw_json[key]

        return raw_json
    
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

    def update_cookies(self, cookies) -> int:
        if not cookies:
            return 1

        self.headers[HEADER.COOKIE] = ""
        for cookie in cookies:
            self.headers[HEADER.COOKIE] += f"{cookie.name}={cookie.value}; "

            if cookie.name == "csrftoken":
                self.headers[HEADER.XCSRFTOKEN] = cookie.value
        return 0
    
    # TODO: content length
    def update_content_length(self, content_length, content_type="application/json;charset=utf-8"):
        self.headers[HEADER.CONTENT_LENGTH] = content_length
        self.headers[HEADER.CONTENT_TYPE] = content_type

    # new methods each for specific header
    def set_timestamp(self, ts: int = None):
        if not ts:
            ts = int(time.time() * 1000)
        self.TIMESTAMP = str(ts)

    def set_xport(self, url: str):
        url_without_domain = url.replace("https://www.simcompanies.com", "")
        if url_without_domain[-1] != "/":
            url_without_domain += "/"

        input_data = f"{url_without_domain}{self.TIMESTAMP}"
        self.XPORT = hashlib.md5(input_data.encode('utf-8')).hexdigest()

    def set_cookies_and_csrftoken(self, cookies) -> int:  # TODO: add cookie type
        if not cookies:
            return 1

        self.COOKIE = ""
        for cookie in cookies:
            self.COOKIE += f"{cookie.name}={cookie.value}; "

            if cookie.name == "csrftoken":
                self.XCSRFTOKEN = cookie.value
        return 0

    def set_content_length(self, content_length: int):
        self.CONTENT_LENGTH = str(content_length)
    
    def set_content_type(self, content_type: str = "application/json;charset=utf-8"):
        self.CONTENT_TYPE = content_type

    def set_origin(self,  origin: str = "https://www.simcompanies.com"):
        self.ORIGIN = origin
