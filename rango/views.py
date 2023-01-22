from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("""
        <p><a href="/rango/">Index</a></p>
        <p>Rango says here is the about page.<p>
    """)
