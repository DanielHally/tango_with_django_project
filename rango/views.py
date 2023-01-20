from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("""
        <p>Rango says hey there partner!</p>
        <p><a href="/rango/about/">About</a></p>
    """)


def about(request):
    return HttpResponse("""
        <p><a href="/rango/">Index</a></p>
        <p>Rango says here is the about page.<p>
    """)
