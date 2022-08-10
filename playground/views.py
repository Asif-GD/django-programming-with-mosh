from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# request -> response
# request handler
# a.k.a an action


def say_hello(request):
    # can be used to pull data from a DB
    # transform data
    # send email
    return render(request, "hello.html", {"name": "Asif Iqbal"}, content_type="text/html")
