#from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

# Easy access to URL
urlHelloVSCode = "http://127.0.0.1:8000/hello/VSCode"
print(urlHelloVSCode)

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M %p")

    # Filter the name argument to the letters only using regular expressions. URL arguments 
    # can contain arbirtray text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
