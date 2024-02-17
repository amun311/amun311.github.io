import requests
import re
import random

listalt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_cuv=[]
for lt in listalt:
    #pt =r"\'>(\D[A-Z]*[a-z]*)</a>" 
    pt =r"\>(\D[A-Z]*[a-z]*)\<\/"    
    url = f'https://www.dictionary.com/list/{lt}'
    response = requests.get(url)   
    html_content = response.content
    words=re.findall(pt, html_content.decode())
    for cuvant in words:
        if cuvant not in list_cuv:
            list_cuv.append(cuvant)
print(list_cuv)
  
mal = ['list','script','fdex']
for i in range(3,4):
    lac = []
    for cuv in list_cuv:        
        if len(cuv) == i and cuv not in lac and cuv not in mal:
            lac.append(cuv)
                
            with open(f'/home/alexandru/Development/Projects/flet/cuvinte/en_cuvinte{i}.cfg','w') as f:
                for cuv in lac:
                    f.writelines(cuv+',')
