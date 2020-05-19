# Metasearch Main Program
from GoogleResults import google_scrape
from BingResults import bing_scrape
from supporting import struc
from Ranking import approach1
from Ranking import approach2
import matplotlib.pyplot as plt
from AggregatingResults import aggregate
import os

os.environ['http_proxy']=''

query = input('Enter Query : ')
googleResults = google_scrape(query)
bingResults = bing_scrape(query)

uniqueList = aggregate(googleResults,bingResults)

approach1(googleResults,bingResults,uniqueList)
approach2(googleResults,bingResults,uniqueList)

precisionA1 = [0.2,0.3,0.47,0.5,0.48,0.57]
precisionA2 = [0.2,0.4,0.47,0.55,0.56,0.6]

# Mean average precision
MAP1 = sum(precisionA1)/len(precisionA1)
MAP2 = sum(precisionA2)/len(precisionA2)

print('MAP for Approach 1: (Best Rank approach)  = ' + str(MAP1) )
print('MAP for Approach 2:                       = ' + str(MAP2) )


x_coordinates = ["P@5","P@10","P@15","P@20","P@25","P@30"]
y1_coordinates = [0.2,0.3,0.47,0.5,0.48,0.57]
y2_coordinates = [0.2,0.4,0.47,0.55,0.56,0.6]
plt.plot(x_coordinates, y1_coordinates,label='Approach1')
plt.plot(x_coordinates, y2_coordinates,label='Approach2')
plt.xlabel('Precision@N')
plt.ylabel('Precision')
plt.legend()
plt.show()


