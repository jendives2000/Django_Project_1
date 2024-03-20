# imported by default
# render actually renders the HTML templates
from django.shortcuts import render

# imported for this project:
from django.http import HttpResponse

# -----------------------------------------------------------------------------


def hello(request):
    # pull data from database
    # transform data
    # send email
    # and a lot more

    # output an instance of the response when responding to the request (HTTP protocol)
    # return HttpResponse("Hello, world. This is an HTTP Response.")

    # renders the HTML template that is passed as an argument
    return render(request, "hello.html")
