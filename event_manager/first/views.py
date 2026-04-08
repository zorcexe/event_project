# first/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def hello(request: HttpRequest):
    """
    eine View erhält IMMER ein request-Objekt als Parameter
    und gibt immer ein HTTP-Response zurück
    """
    print(f"HTTP-Methode: {request.method}")  # Get, Post
    print(f"User: {request.user}")
    print(f"Get: {request.GET}")  # example.de?x=1
    return HttpResponse("Hello World")
