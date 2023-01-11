from urllib.parse import urljoin

def crawl(guessed, browser):
    
    discovered = set()
    discovered.union(guessed)
    urls = guessed

    print(urls)
    while(len(urls) > 0):
        curr_url = urls.pop()

        if "logout" in curr_url:
            print("\nLogout found: " + curr_url)
        else:
            browser.open(curr_url)
            if browser.page != None:
                links = browser.page.select('a')
                for link in links:
                    curr = urljoin(curr_url, link.get('href'))
                    if "localhost" in curr and "logout" not in curr and "@" not in curr:
                        if curr not in discovered:
                            urls.add(curr)
                            discovered.add(curr)
                            print("\nDiscovered: " + curr)
    return discovered
            


    
