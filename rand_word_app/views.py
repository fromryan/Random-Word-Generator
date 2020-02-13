from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'attempt' not in request.session.keys():
        request.session['attempt'] = 0
        request.session['random_word'] =""
    return render(request,'index.html')



def random_word(request):
    request.session['attempt'] += 1
    request.session['random_word'] = get_random_string(length=14)

    return redirect('/')



def reset(request):
    if 'attempt' or 'random_word' in request.session.keys():
        del request.session['attempt']
        del request.session['random_word']

    return redirect('/')