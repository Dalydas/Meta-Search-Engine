from supporting import struc
from supporting import intersect
from supporting import union

def aggregate(googleResults,bingResults):
    l1 = []
    l2 = []
    uniques = struc()
    for each in googleResults:
        l1.append(each.url)
    
    for each in bingResults:
        l2.append(each.url)

    uniqueList = union(l1,l2)

    # Common Results
    #print(intersect(l1,l2))
    print(str(len(l1)) + ' Google Results, ' + str(len(l2)) + ' Bing results, ' + str(len(uniqueList)) + ' Unique Results')

    googleURLs = []
    bingURLs = []

    for result in googleResults:
        googleURLs.append(result.url)

    for result in bingResults:
        bingURLs.append(result.url)

    # Writing Aggregated Documents
    filename = 'UniqueDocuments.txt'
    file = open(filename,"w")
    count = 0
    for link in uniqueList:
        if link in googleURLs:
            count = count + 1
            i = googleURLs.index(link)
            file.write(str(count) + '    ' + str(googleResults[i].title) + ' ' + str(googleResults[i].description) + '\n')
        elif link in bingURLs:
            count = count + 1
            i = bingURLs.index(link)
            file.write(str(count) + '    ' + str(bingResults[i].title) + ' ' + str(bingResults[i].description) + '\n')
    return uniqueList
