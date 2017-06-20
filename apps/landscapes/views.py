# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    # print ('Long, whip-like tails were a distinctive feature of the ' +
    #        'diplodocoids - but what was their purpose?')
    return render(request, 'landscapes/index.html')

def image(request, num):
    # assignment instructions specify that this isn't actually random, despite
    # the title of the assignment...oh well
    try:
        number = int(num)
        if number >= 1 and number <= 10:
            landscape = 'snow'
        elif number >= 11 and number <= 20:
            landscape = 'desert'
        elif number >= 21 and number <= 30:
            landscape = 'forest'
        elif number >= 31 and number <= 40:
            landscape = 'vineyard'
        elif number >= 41 and number <= 50:
            landscape = 'tropical'
        else:
            return ValueError
        context = {
            'landscape': landscape
        }
        return render(request, 'landscapes/image.html', context)
    except (ValueError, AttributeError):
        messages.error(request, 'Please only use a number between 1 and 50 ' +
                       'as the url parameter.')
        return redirect('/')
