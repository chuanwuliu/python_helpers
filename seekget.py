
from urllib.request import urlopen
import re

URL = 'https://www.seek.com.au'
#CLASSIFICATION = 'classification=1223%2C6281%2C1209%2C1203&' # My own classification.
CLASSIFICATION = ''
KEYWORD = 'Physics'

def get_page(url):
    """Get web page using url
    Args:
        url: the url of the page
    Return:
        page: the page as a string.
    """
    page = urlopen(url).read().decode(encoding='UTF-8',errors='strict')
    return page

for i in range(1, 1000):
    print('Searching page: ', i)
    page = get_page(URL + '/jobs?' + CLASSIFICATION + 'page=' + str(i))
    if 'Change or remove filters such as classification to broaden your search' in page:
        print('Stop!')
        break

    pattern = re.compile('href="/job/\d+\?type=[a-z]*&[a-z]*;userqueryid=\w+-\w+')
    prog = re.compile(pattern)
    address_list = prog.findall(page)
    address_list = list(set(address_list))
    
    for address in address_list:
        url = URL + address[6:]
        page = get_page(url)
        if KEYWORD in page:
            pattern = re.compile('class="jobtitle">[^<]*')
            prog = re.compile(pattern)
            title = prog.findall(page)[0]
            pattern = re.compile('"advertiserName":"[^"]*"')
            prog = re.compile(pattern)
            advertiser = prog.findall(page)[0]
            print('===> Title: ', title[16:], 'Advertiser: ', advertiser[17:])
            print('     URL: ', url)
