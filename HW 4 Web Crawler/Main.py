import indexer
import searcher

import urllib.request
import json
from pprint import pprint

def call_weather_api(keywords):
    for i, keyword in enumerate(keywords):
        #Only use the first keyword for the Weather API
        if i == 1:
            break
        api_url = 'http://api.openweathermap.org/data/2.5/weather?q=%s'

        page = urllib.request.urlopen(api_url % keyword)
        content=page.read()
        content_string = content.decode("utf-8")

        json_data = json.loads(content_string)

        city = json_data.get('name', None)
        weather = json_data.get("weather")

        if city:
            print('The weather for {} is {}'.format(city, weather[0]['main']))


query=input("query: ")

if not query:
    print("Must enter something")
    exit(0)

qtype, keywords = searcher.detect_query_type(query)
 
#Initiate Task 4
call_weather_api(keywords)

#Process both pickle files and store in fortunes_shelve
indexer.preprocess(['web_data.pickle','data.pickle',], 'fortunes_shelve')

output = searcher.search('fortunes_shelve', qtype, keywords)

if output:
    for found in output:
        print("Found at ", found)
else:
    print ("Not Found")