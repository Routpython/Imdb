from django.shortcuts import render
from IMDB_Project.settings import MOVIES,MOVIES1
# Create your views here.
import json
def index(request):
    dict_data = json.loads(open(MOVIES).read())
    dict_data1 =json.loads(open(MOVIES1).read())
    for x in dict_data1:
        print(x)
    a1=dict_data1['title']
    a2=dict_data1['videoProducts']['physical'][3]
    a3 = dict_data1['videoProducts']['physical'][0]
    type(a3)
    print(a3)

    return render(request,'index.html',{'res':dict_data,'inc':a1,"a2":a2,'a3':a3})
















def cast(request):
    dict_data = json.loads(open(MOVIES).read())
    for z in dict_data:

        res8 = dict_data['result']['credits']['cast']
        for x in res8:
            print(x['name'], '-----', x['role'])

        #    return render(request,'index.html',{'a':res1,'b':res2,'c':res3,'d':res4,'e':res5,'f':res6,'g':res6,'h':res7,'i':res8})
        return render(request, 'index.html', { 'res1': res8})

