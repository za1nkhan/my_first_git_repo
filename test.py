import requests
import csv
import json

url = 'https://timnews.com.br/tagger/content?url=https%3A%2F%2Ftimnews.com.br%2Fapi%2Fv3%2Fmedia%2Fnews_stories%2F41871486%26frequency%3D2%26offset%3D1'
r = requests.get(url)
#print(r.text)

text_json = json.loads(r.text)
print(text_json)

 
#with open ('stocks.csv','w', newline='') as f:
    #write.wrighter = 