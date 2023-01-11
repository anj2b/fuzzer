

def test(inputs, args, browser):
    vectors = open(args.vectors).readlines()
    f = open(args.sensitive, 'r')
    sensitive_words = f.read().split()
    f.close()
    print("\n*** Testing Vectors Against URL Parameters ***\n")
    test_vectors_params(vectors, inputs, sensitive_words, browser, args.timeout)
    
def test_vectors_params(vectors, input, sensitive, browser, timeout):
    for url in input:
        try:
            print("Testing url parameters on: " + url)
            c = input[url]['parameters']
            parameters = c.keys()
            test_params = {}
            for vector in vectors:
                for param in parameters:
                    test_params[param] =  vector
                    response = browser.get(url, params=test_params)
                    check_response_code(response, browser)
                    check_sensitive_words(response, sensitive)
                    check_response_time(response, timeout)
                    check_sanitization(response, vector, browser)
        except:
            continue

def check_response_code(response, browser):
    if response.status_code != 200:
        print("Broken input:", browser.codes[response.status_code])

def check_sensitive_words(response, sensitive_words):
    for word in sensitive_words:
        if word in response.text:
            print("Response contained the following sensitive word: " + word)

def check_sanitization(response, vector, browser):
    if vector in response.text:
        print("Sanitization failed: " + vector)

def check_response_time(response, timeout):
    load_time = response.elapsed.total_seconds() * 1000
    if load_time > timeout:
        print("Response took " + load_time.__str__())