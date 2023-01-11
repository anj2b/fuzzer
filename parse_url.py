
def parse(urls):
    """
    Parses the list of URLs and finds and adds parameters to a dictionary.
    """
    parsed_urls = {}
    for url in urls:
        parsed_urls[url] = {}
        url_split = url.split('?')
        parsed_urls[url]['base_url'] = url_split[0]
        if len(url_split) > 1:
            parsed_urls[url]['parameters'] = {}
            parameters = url_split[1].split('&')
            for parameter in parameters:
                parameter_split = parameter.split('=')
                parsed_urls[url]['parameters'][parameter_split[0]] = parameter_split[1]
    return parsed_urls
    


    

