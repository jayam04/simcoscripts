from common.sim_request import Request

class Session:
    def __init__(self, user, cookies=None):
        self.user = user
        self.cookies = cookies

    def authenticate(self) -> int:
        if not self.cookies:
            return 1
        if "csrftoken" not in self.cookies:
            return 1
        url = "https://www.simcompanies.com/api/v2/auth/email/auth/"
        request = Request(url, method="POST")
        request.headers.update_cookies(self.cookies)
    
    def generate_cookies(self) -> int:
        request = Request("https://www.simcompanies.com")
        response = request.send()
        self.cookies = response.cookies

