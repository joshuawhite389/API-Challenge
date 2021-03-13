import requests
import json
import datetime

class JSON_Placeholder_API:

    def __init__(self, url):
        self.url = url

    def getJsonObject(self, postNumber):
        response = requests.get(self.url + postNumber)
        # print json object
        def jprint(obj):
         # create a formatted string of the Python JSON object
            text = json.dumps(obj, sort_keys=True, indent=4)
            print(text)

        jprint(response.json())

    def getTitle(self, postNumber):
        response = requests.get(self.url + postNumber)
        response_dictionary = response.json()
        response_title = response_dictionary['title']
        print(f"Title: {(response_title)}")

        
    def injectTime(self, postNumber):
        response = requests.get(self.url + postNumber)
        response_dictionary = response.json()
        time = datetime.datetime.now()
        time = (time.strftime("%m/%d/%Y %H:%M:%S"))
        response_dictionary["time"] = time
        print(response_dictionary)



