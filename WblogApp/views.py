from django.shortcuts import render
#from httpresponse import request

# Create your views here.
def barca(request):
    return render(request, 'index.html')