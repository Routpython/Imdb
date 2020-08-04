import json
import requests
import http.client
class Imdb1:
    def __init__(self,get_response):
        self.get_response=get_response

        url = "https://imdb8.p.rapidapi.com/title/get-top-stripe"

        querystring = {"currentCountry": "US", "purchaseCountry": "US", "tconst": "tt0944947"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "be40fa23dfmsh7582999b627271bp1b837fjsn264e833ddcf3"
        }

        response = requests.get( url, headers=headers, params=querystring)

        dict_data=json.loads(response.text)
        json.dump(dict_data,open('app1/raw/coviod.json','w'))

        print('data created1')


    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        print('I am call')
        return response