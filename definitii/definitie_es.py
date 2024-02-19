import re
import urllib.request as urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
def definitie_es(cuv):
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    try:
      
      req = urllib.Request(f'https{chr(58)}//dle.rae.es/{cuv}', None, headers)
      response = urllib.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')
      #print(soup)
      response.close() 
    except: soup = ''
    pt = r'1. (\w{1,}. \w*\s*.*).\",'
    definitie = re.search(pt,str(soup))
    #definitie = str(definitie)
    try:
        definitie= definitie.group(1)
    except:
        definitie = ''
    dfn = str(definitie).lstrip("['").rstrip("']")
    
    return dfn