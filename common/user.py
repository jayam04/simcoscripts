from common.session import Session
from common.sim_request import Request

class User:
    def __init__(self, username=None, password=None, id=None, companies=[], cookies=None):
        self.username = username
        self.password = password
        self.id = id
        self.companies = companies
        self.cookies = None
        self.current_company = None

    def get_user_id_and_companies(self):
        auth_session = Session(self)
        auth_session.authenticate()
        pass
    
    def authenticate(self) -> int:
        if not self.cookies:
            return 1
        if "csrftoken" not in self.cookies:
            return 1
        url = "https://www.simcompanies.com/api/v2/auth/email/auth/"
        request = Request(url, method="POST")
        request.headers.update_cookies(self.cookies)
        request.headers.update_timestamp()
        request.update_body({"email": self.user.username, "password": self.user.password})
        response = request.send()
        if response.ok:
            self.cookies = response.cookies
        return response
    
    def generate_cookies(self) -> int:
        request = Request("https://www.simcompanies.com")
        response = request.send()
        self.cookies = response.cookies



