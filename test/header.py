from common.headers import Header
from helpers.dev_tools import *

def check_xport():
    start_dev_mode()
    header = Header()
    testcase = {
        "xport": "af87d1b5cf287346b808081e104dc8e2",
        "ts": "1691635873640",
        "url": "https://www.simcompanies.com/api/v2/companies/me/note/3035179/"
    }
    header.update_timestamp(testcase["url"], testcase["ts"])

    if header.headers["X-Port"] != testcase["xport"]:
        dev_print("wrong X-Port: " + header.headers["X-Port"], testcase["xport"], info_type="error")
        return 1
    else:
        dev_print("verified X-Port: " + header.headers["X-Port"], info_type="checkpoint")
        return 0

check_xport()