from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import joblib
import pickle
import numpy as np
with open('C:\ML project\model.pkl', 'rb') as f:
    model = pickle.load(f)
# Create your views here.
def hello(request):
    text="<h1>Hello World</h1>"
    return HttpResponse(text)
def ability(request):
    return render(request,'ability.html')
def pre(request):
        model=joblib.load('saved_model.sav')
        lis=[]
        lis.append(request.GET['feature1'])
        lis.append(request.GET['feature2'])
        lis.append(request.GET['feature3'])
        lis.append(request.GET['feature4'])
        lis.append(request.GET['feature5'])
        lis.append(request.GET['feature6'])
        lis.append(request.GET['feature7'])
        lis.append(request.GET['feature8'])
        lis.append(request.GET['feature9'])
        #print(lis)
        data_array = np.asarray(lis)
        arr= data_array.reshape(1,-1)
        pred=model.predict(arr)
        return render(request,'result.html',{'result':pred})