from django.urls import path

# importing the views file that handles all of the HTTP
from . import views

# URL configuration:
urlpatterns = [
    # all playground URL prefix are handled by ecommerce_app urls.py
    # this means here http://playground/hello/ --> becomes http://hello
    path("hello/", views.hello)
]
