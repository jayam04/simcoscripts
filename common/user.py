from .session import Session

class User:
    def __init__(self, username=None, password=None, id=None, companies=[]):
        self.username = username
        self.password = password
        self.id = id
        self.companies = companies

    def get_user_id_and_companies(self):
        auth_session = Session(self)
        auth_session.authenticate()
        pass
