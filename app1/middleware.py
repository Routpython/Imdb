import json
import requests
class Imdb:
    def __init__(self,get_response):
        self.get_response=get_response


        url = "https://box-office-buz1.p.rapidapi.com/movie/3113"

        headers = {
            'x-rapidapi-host': "box-office-buz1.p.rapidapi.com",
            'x-rapidapi-key': "be40fa23dfmsh7582999b627271bp1b837fjsn264e833ddcf3"
        }

        response = requests.get( url, headers=headers)

    #    print(response.text)
        print(response.status_code)
        dict_data=json.loads(response.text)
        json.dump(dict_data,open('app1/raw/package.json','w'))

        print('data created')


    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        print('I am call')
        return response