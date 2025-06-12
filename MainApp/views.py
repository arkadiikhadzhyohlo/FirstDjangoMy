from django.shortcuts import render,HttpResponse

# Create your views here.
def home (request):
    text = "<h1>Welcome</h1>!"
    return HttpResponse(text)

def about (request):
    text= "Автор - Аркадий"
    return HttpResponse(text)