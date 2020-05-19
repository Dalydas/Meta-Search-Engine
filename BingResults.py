from bs4  import BeautifulSoup
from supporting import struc
from urllib.request import urlopen
from urllib.request import Request

# Number of results you need to store from each search engine
numresults = 32

def bing_scrape(query):
    bingResults = []
    address = "https://www.bing.com/search?q=" + query + "&count=" + str(numresults)
    request = Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page,'html5lib')

    titles = []
    descriptions = []
    urls = []

    headers = soup.findAll('li',attrs = {'class':'b_algo'})
    for header in headers:
        if header is not None:
            anchor = header.find('a')
            desc = header.find('p')
            if anchor is not None and desc is not None:
                t = anchor.contents[0].encode("utf-8")
                u = anchor['href']
                urls.append(u)
                titles.append(t)
                d = desc.text.encode("utf-8")
                descriptions.append(d)
            
    size = len(titles)
    
    filename = query + '_Bing.txt'
    file = open(filename,"w")
    for i in range(0,size):
        result = struc()
        result.rank = i+1
        result.title = titles[i]
        result.description = descriptions[i]
        result.url = urls[i]
        file.write(str(i+1) + '    ' + str(titles[i]) + ' ' + str(descriptions[i]) + '\n')
        bingResults.append(result)

    return bingResults
