from django.shortcuts import render

def index(req):
    return render(req,'home/index.html')

def sendData(req):
    return render(req,'home/sendData.html')
