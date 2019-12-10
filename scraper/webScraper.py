import requests
import re
from bs4 import BeautifulSoup


def printStats(root_url):
    response = requests.get(root_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find a div with class name keystatistics
    key_statistics = soup.find('div', attrs={'class': 'keystatistics'})
    # find all uls in this section
    all_ps = key_statistics.findAll('p')
    dict1 = {}
    for i in range(0, len(all_ps), 2):
        #print(all_ps[i].text, end=" --> ")
        #print(all_ps[i + 1].text)
        dict1[all_ps[i].text] = all_ps[i + 1].text
    return dict1

