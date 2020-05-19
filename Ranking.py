from supporting import struc
import operator

def LpNorm(Google,Bing,p):
    return Google**p + Bing**p

def printResults(newRankList,uniqueList,googleResults,bingResults,googleURLs,bingURLs,ul,filename):
    for i in range(0,len(uniqueList)):
        result = struc()
        result.url = uniqueList[i]
        result.rank = ul[i]
        if uniqueList[i] in googleURLs:
            ind = googleURLs.index(uniqueList[i])
            result.title = googleResults[ind].title
            result.description = googleResults[ind].description           
        else:
            ind = bingURLs.index(uniqueList[i])
            result.title = bingResults[ind].title
            result.description = bingResults[ind].description
        newRankList.append(result)
        
    newRankList.sort(key=operator.attrgetter('rank'))
    
    file = open(filename,"w")
    count = 0
    for result in newRankList:
        count = count + 1
        file.write(str(count) + '    ' + str(result.title) + '    ' + str(result.description) + '\n')
    return

def approach1(googleResults,bingResults,uniqueList):
    googleURLs = []
    bingURLs = []
    for result in googleResults:
        googleURLs.append(result.url)

    for result in bingResults:
        bingURLs.append(result.url)    
    ul = []
    for i in range(0,len(uniqueList)):
        x = 100
        y = 100
        if uniqueList[i] in googleURLs:
            x = googleURLs.index(uniqueList[i])
        if uniqueList[i] in bingURLs:
            y = bingURLs.index(uniqueList[i])
        if x<y:
            z = x + 0.25
        else:
            z = y + 0.5
        ul.append(z)
    approach1 = []
    filename = 'ResultantRanks_A1.txt'
    printResults(approach1,uniqueList,googleResults,bingResults,googleURLs,bingURLs,ul,filename)
    return

def approach2(googleResults,bingResults,uniqueList):
    googleURLs = []
    bingURLs = []
    for result in googleResults:
        googleURLs.append(result.url)

    for result in bingResults:
        bingURLs.append(result.url)    
    ul = []
    for i in range(0,len(uniqueList)):
        x = 0
        y = 0
        if uniqueList[i] in googleURLs:
            x = googleURLs.index(uniqueList[i])
        if uniqueList[i] in bingURLs:
            y = bingURLs.index(uniqueList[i])
        z = LpNorm(x,y,1)
        ul.append(z)
    approach2 = []
    filename = 'ResultantRanks_A2.txt'
    printResults(approach2,uniqueList,googleResults,bingResults,googleURLs,bingURLs,ul,filename)
    return
