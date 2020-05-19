from bs4  import BeautifulSoup
from supporting import struc
from urllib.request import urlopen
from urllib.request import Request

# Number of results you need to store from each search engine
numresults = 30 

def google_scrape(query):
    googleResults = []
    address = "http://www.google.com/search?q=" + query + "&num=" + str(numresults+4) +"&hl=en&start=0"
    request = Request(address, None, {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page,'html5lib')

    titles = []
    descriptions = []
    urls = []

    headers = soup.findAll('div',attrs = {'class':'rc'})
    for header in headers:
        anchor = header.find('a')
        t = anchor.h3.text.encode('utf-8')
        u = anchor['href']
        urls.append(u)
        titles.append(t)
        
    desclist = soup.findAll('span','st')
    for desc in desclist:
        d = desc.text.encode('utf-8')
        descriptions.append(d)

    size = len(titles)
    filename = query + '_Google.txt'
    file = open(filename,"w")
    for i in range(0,size):
        result = struc()    
        result.rank = i+1
        result.title = titles[i]
        result.description = descriptions[i]
        result.url = urls[i]
        file.write(str(i+1) + '    ' + str(titles[i]) + ' ' + str(descriptions[i]) + '\n')
        googleResults.append(result)
    return googleResults
