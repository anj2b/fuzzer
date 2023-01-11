import requests

def guess(url, browser, wordfile):
    guessed = set()
    with open(wordfile, 'r') as f:
        words = f.read().split()
    with open('endings.txt', 'r') as f:
        endings = f.read().split()
    if url[-1] != '/':
        url += '/'
        for word in words:
            for ending in endings:
                guess_url = url + word + ending
                if validate_url(guess_url):
                    guessed.add(guess_url)
                    print("\nGuessed Page: " + guess_url)
                else:
                    pass
    return guessed
        

def validate_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False

