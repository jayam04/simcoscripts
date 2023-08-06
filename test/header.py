from common.headers import Header
from helpers.dev_tools import *

def check_xport():
    start_dev_mode()
    header = Header()
    header.update_timestamp("https://www.simcompanies.com/api/v1/players/me/companies/", ts=1691301190663)
    dev_print(header.headers["X-Port"], info_type="checkpoint")

check_xport()