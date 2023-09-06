import time
from helpers import dev_tools

from common.sim_request import Request


class Company:
    def __init__(self, company_id, name, realm_id, user):
        self.id = company_id
        self.name = name
        # TODO: it would be nice to have a real realm object here
        self.realm_id = realm_id
        self.user = user

    def __str__(self):
        # TODO: improve this to be more readable
        return f"{self.name} ({self.id}) in realm with ID {self.realm_id}"

    def send_message_to(self, message, recipient_id):
        body = {
            "companyId": recipient_id,
            "body": message,
            "token": int(time.time() * 1000)
        }
        request = Request("https://www.simcompanies.com/api/v2/message/", method="POST", body=body)
        request.headers.update_cookies(self.user.cookies)
        # TODO: improvement by updating timestamp and xport using request methods
        request.headers.update_timestamp(url=request.url)
        response = request.send()
        dev_tools.dev_print(response, response.json)

