import time
from common.realms import Realm
from helpers import dev_tools

from common.sim_request import Request
from common.building import Building
import json


class Company:
    def __init__(self, company_id, name, realm_id, user, buildings=set()):
        self.id = company_id
        self.name = name
        self.realm_id = realm_id
        self.user = user
        self.buildings = buildings

    def __str__(self):
        # TODO: improve this to be more readable
        return f"{self.name} ({self.id}) in realm {self.realm_id}"


    def send_message_to(self, message, recipient_id):
        body = {
            "companyId": recipient_id,
            "body": message,
            "token": int(time.time() * 1000)
        }
        dev_tools.dev_print(body, info_type="debug")
        request = Request("https://www.simcompanies.com/api/v2/message/", method="POST", body=body)
        request.headers.update_cookies(self.user.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        dev_tools.dev_print(response.status_code, info_type="debug")

    def get_buildings(self):
        request = Request("https://www.simcompanies.com/api/v2/companies/me/buildings/")
        request.update_cookies_and_csrftoken(self.user.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        if response.ok:
            buildings = response.json()
            for building in buildings:
                building_object = Building(building["id"], building["kind"], building["name"], building["size"],
                                           building["robotsSpecialization"], building["pinnedResource"])
                self.buildings.add(building_object)
                dev_tools.dev_print(f"Added building: {building_object}")
            return 0
        return response.status_code
