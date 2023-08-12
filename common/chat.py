import requests
from requests import Response

from common.sim_request import Request

import time

from common.user import User
from helpers import dev_tools


class Chat:
    url = "https://www.simcompanies.com/api/v2/message/"

    def __init__(self, user: User, recipient_id: int, chatroom: bool = False) -> None:
        self.recipient_id = recipient_id
        self.is_chatroom = chatroom
        self.user = user
        self.cookies = None

    def send_message(self, message: str) -> Response:
        self.patch_chat()

        request = Request(self.url,  method="POST")
        request.update_body({"companyId": self.recipient_id, "body": message, "token": int(time.time() * 1000)})
        request.update_cookies_and_csrftoken(self.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        if response.ok:
            dev_tools.dev_print(response)
            return response
        else:
            dev_tools.dev_print(response, response.status_code)
            return response

    def patch_chat(self):
        # TODO: i don't know but it works for now
        request = Request("https://www.simcompanies.com/api/messages/", method="PATCH")
        request.update_body({"companyId": self.recipient_id})
        request.update_cookies_and_csrftoken(self.user.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        time.sleep(1)
        if response.ok:
            dev_tools.dev_print(response)
            self.cookies = response.cookies
            return response
        else:
            dev_tools.dev_print(response, response.status_code)
            return response
