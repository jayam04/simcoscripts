from common.company import Company
from common.sim_request import Request
from helpers import dev_tools


class User:
    def __init__(self, username=None, password=None, user_id=None, companies=None, cookies=None):
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
        # auth_session = Session(self)
        # auth_session.authenticate()
        # TODO: get companies, create Company for companies, --> set current company
        # todo in get_id and current_company

        request = Request("https://www.simcompanies.com/api/v1/players/me/companies/")
        request.headers.update_cookies(self.cookies)
        request.headers.update_timestamp(url=request.url)
        response = request.send()
        dev_tools.dev_print(response.json())
        if response.ok:
            response = response.json()
        for item in response:
            company = Company(item["id"], item["company"], item["realmId"], self)
            self.companies.append(company)
        return 0
    
    def authenticate(self):
        if not self.cookies:
            return 1
        if "csrftoken" not in self.cookies:
            return 1
        url = "https://www.simcompanies.com/api/v2/auth/email/auth/"
        request = Request(url, method="POST")
        request.headers.update_cookies(self.cookies)
        request.headers.update_timestamp(url=request.url)
        request.update_body({"email": self.username, "password": self.password})
        response = request.send()
        if response.ok:
            self.cookies = response.cookies
        return response
    
    def generate_cookies(self) -> int:
        request = Request("https://www.simcompanies.com")
        response = request.send()
        self.cookies = response.cookies
        return 0

    def get_current_company(self):
        request = Request("https://www.simcompanies.com/api/v2/companies/me/")
        request.headers.update_cookies(self.cookies)
        request.headers.update_timestamp(request.url)
        response = request.send()
        print(response)
        # TODO: set current company if successful, else return error code
