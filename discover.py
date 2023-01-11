import mechanicalsoup
import crawler 
import guesser
import parse_url
import parse_form
import parse_cookies

def discover(args):
    if args.custom_auth != None:
        if args.custom_auth.lower() == "dvwa":
            browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
            browser.open('{}/setup.php'.format(args.url))
            browser.select_form()
            browser.submit_selected()
            browser.open('{}/'.format(args.url))
            browser.select_form()
            browser["username"] = "admin"
            browser["password"] = "password"
            browser.submit_selected()
            browser.open('{}/security.php'.format(args.url))
            browser.select_form()
            browser["security"] = "low"
    else:
        browser = mechanicalsoup.StatefulBrowser()
    print("\n Guessing Pages \n")
    guessed_links = guesser.guess(args.url, browser, args.common_words)

    print("\n Crawling Links \n")
    discovered_links = crawler.crawl(guessed_links, browser)
    all_urls = discovered_links.union(guessed_links)

    print("\n Parsing Urls \n")
    parsed = parse_url.parse(all_urls)
    for key in parsed:
        print("\n {} \n".format(key))

    print("\n Parsing forms \n")
    forms = parse_form.parse(all_urls, browser)
    for key in forms:
        print("\n {} \n".format(key))

    print("\n Discovering Cookies \n")
    cookies = parse_cookies.get_cookies(browser)
    print(cookies)

    return parsed, browser