
def parse(urls, browser):
    """For each url get all forms and inputs and add to set"""
    forms = set()
    for url in urls:
        browser.open(url)
        if browser.page is not None:
            for i in browser.page.find_all('input'):
                if i is not None and i.get('type') != 'submit' and i.get('type') != 'button':
                    forms.add(i)
    return forms