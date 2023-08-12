from common.company import Company
from common.sim_request import Request
from helpers import dev_tools


class User:
    def __init__(self, username: str, password: str, user_id=None, companies=None, cookies=None):
        self.username = username
        self.password = password
        self.id = user_id
        if companies:
            self.companies = companies
        else:
            self.companies = []
        self.cookies = cookies
        self.current_company = None

    def get_companies(self):
        request = Request("https://www.simcompanies.com/api/v1/players/me/companies/")
        request.update_cookies_and_csrftoken(self.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        if response.ok:
            dev_tools.dev_print(response.json())
            response = response.json()
        for item in response:
            company = Company(item["id"], item["company"], item["realmId"], self)
            self.companies.append(company)
        return 0
    
    def authenticate(self):
        if not self.cookies or "csrftoken" not in self.cookies:
            self.generate_cookies()

        request = Request("https://www.simcompanies.com/api/v2/auth/email/auth/", method="POST")
        request.update_cookies_and_csrftoken(self.cookies)
        request.update_timestamp_and_xport()
        request.update_body({"email": self.username, "password": self.password})
        response = request.send()
        if response.ok:
            self.cookies = response.cookies
        return response
    
    def generate_cookies(self) -> int:
        request = Request("https://www.simcompanies.com")
        response = request.send()
        if response.ok:
            self.cookies = response.cookies
            return 0
        dev_tools.dev_print(response, response.status_code)
        return 1

    def set_cookies(self, cookies) -> int:  # TODO: add parameter type
        if cookies:
            self.cookies = cookies
            return 0
        return 1

    def get_userid_and_current_company(self):
        request = Request("https://www.simcompanies.com/api/v2/companies/me/")
        request.update_cookies_and_csrftoken(self.cookies)
        request.update_timestamp_and_xport()
        response = request.send()
        if response.ok:
            # dev_tools.dev_print(response.json())
            response = response.json()
        for company in self.companies:
            if company.id == response["authCompany"]["companyId"]:
                self.current_company = company
                break
        else:
            return 1
        self.id = response["authUser"]["playerId"]
        dev_tools.dev_print(self.current_company)

        return 0
