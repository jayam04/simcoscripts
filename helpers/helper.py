def copy_cookies(source_jar, target_jar):
    """
    Copy cookies from one jar to another.
    """
    # pylint: disable=protected-access
    # The above line is needed because CookieJar._cookies
    # is a dictionary with Python 2 and 3 compatible keys.
    if target_jar:
        for cookie in source_jar:
            target_jar.set_cookie(cookie)
    
    target_jar = source_jar

    for cookie in target_jar:
        print(cookie)
