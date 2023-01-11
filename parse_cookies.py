
def get_cookies(browser):
    """
    Get the cookies from the browser
    """
    cookies = {}
    for c in browser.session.cookies:
        cookies[c.name] = c.value
    return cookies