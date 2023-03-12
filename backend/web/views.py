from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Welcome to the backend")