def populate_header(header, cookie):
    header["X-CSRFToken"] = cookie["csrftoken"]
    header["Cookie"] = "csrftoken=" + cookie["csrftoken"] + "; sessionid=" + cookie["session_id"]


