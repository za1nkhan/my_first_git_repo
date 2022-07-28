import requests, json, csv

header = {'Content-Type': 'application/json'}
payload_initial = {
  "_source": ["eventCategory","eventImportance","eventTitle"],
  "size": 500,
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "timestamp": {
              "gte": "now-24h",
              "lte": "now"
            }
          }
        }
      ] 
    }
  },"sort": [
    {
      "timestamp": {
        "order": "desc"
      }
    }
  ]
}

payload_batch = {
"scroll": "5m"
}

counter = 0 
while True:
    #print('inside while')
    if counter == 0:
        #print('inside if')
        r = requests.post('http://kibana.evntl.com:9200/news_collector/_search?scroll=5m', json=payload_initial, headers=header)

        tojson = json.loads(r.text)
        hits = tojson["hits"]["hits"]

        scrollid = tojson["_scroll_id"]
        payload_batch["scroll_id"]=scrollid
        print (payload_batch)
        print (tojson["hits"]["total"])
        #print ()

        with open ('eventsdata.csv', 'w', newline='',encoding ="UTF-8") as csvfile:

            write = csv.writer(csvfile)
 
            write.writerow(['eventCategory','eventImportance','eventTitle'])

            for hit in hits:
                source = (hit["_source"])
                
                eventCategory = ''
                eventImportance = ''
                eventTitle = ''
                if "eventCategory" in source:
                    eventCategory = source["eventCategory"]
                if "eventImportance" in source:
                    eventImportance = source["eventImportance"]
                if "eventTitle" in source:
                    eventTitle = source["eventTitle"]

                write.writerow([eventCategory, eventImportance, eventTitle])

    else:
        #print('inside else')
        r2 = requests.post('http://kibana.evntl.com:9200/_search/scroll', json=payload_batch, headers=header)
        
        tojson = json.loads(r2.text)
        hits = tojson["hits"]["hits"]
        if len(hits)==0:
            print('end')
            break


        with open ('eventsdata.csv', 'a', newline='', encoding ="UTF-8") as csvfile:

            write = csv.writer(csvfile)

            for hit in hits:
                source = (hit["_source"])
                
                eventCategory = ''
                eventImportance = ''
                eventTitle = ''
                if "eventCategory" in source:
                    eventCategory = source["eventCategory"]
                if "eventImportance" in source:
                    eventImportance = source["eventImportance"]
                if "eventTitle" in source:
                    eventTitle = source["eventTitle"]

                #print (eventCategory)
                write.writerow([eventCategory, eventImportance, eventTitle])
        
        
        #break
    counter += 1
    


