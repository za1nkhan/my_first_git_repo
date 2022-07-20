import requests, csv, json

#elastic search query needed to get the data
payload = {
  "_source": [ "text", "channel" ],
  "query": {
    "match_all": {}
  }
}
headers = {'Content-Type': 'application/json'}
r = requests.post('http://kibana.evntl.com:9200/news_collector/_search?pretty', json=payload, headers=headers)

#if statment ensures datatype is json format
content_type = r.headers['content-type']
#print(content_type)
if content_type == 'application/json; charset=UTF-8':

    #loading data into json response
    tojson = json.loads(r.text)

    #hits in hits to get get specific json response to get channel and text data
    hits = tojson["hits"]["hits"]
    #print (r.text)

#creating csv file to input json response
    with open ('channel_text.csv', 'w', newline = '') as file:
        write = csv.writer(file)
        
        #titles
        write.writerow(['channel', 'text'])
        #looping through hits to get the channel and text
        for hit in hits:

            #saving key value _source that is inside hits
            source = (hit["_source"])
            
            #ran into problem with a piece of data that did not have channel and text
            # empty variables
            channel = ''
            text = ''
            
            #ensures there is a value in channel key
            if "channel" in source:
                channel = source["channel"]

            #ensures there is a value in text key
            if "text" in source:
                text = source["text"]

            #writes the value from channel and text key into the csv file so it can be used for training   
            write.writerow([channel, text])

            #for key, value in source.items():
                #write.writerow(value)
                #print(key)


                #made a change

        