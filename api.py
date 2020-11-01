import requests
from bs4 import BeautifulSoup
import re
import random
def getNature():
    nature = requests.get("https://www.nature.com/nature/research")
#    border-gray-medium border-bottom-1 pb20
    papers = re.findall("<a href=\"(.*?)temprop=\"url\" data-track=\"click\" data-track-action=\"view article\" data-track-label=\"link\">",nature.text)
    links = []
    for paper in papers:
        links.append(paper.strip("\" i"))
    return("https://www.nature.com" + random.choice(links))
def getNejm():
    nejm = requests.get("https://www.nejm.org/toc/nejm/medical-journal?query=main_nav_lg")
    papers = re.findall("<a href=\"(\/doi\/full.*?)class=\"m-teaser-item__link\">", nejm.text)
    links = []
    for paper in papers:
        links.append(paper)
    return("https://www.nejm.org" + random.choice(links).strip("\""))
journals = [getNature(), getNejm()]
print(random.choice(journals))
