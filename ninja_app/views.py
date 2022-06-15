from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
import random
import datetime


def index(request):
    if not 'counter' in request.session:
        request.session['counter']=0
    if not 'gold' in request.session:
        request.session['gold']=0
    if not 'random' in request.session:
        request.session['random']=0
    if not 'log' in request.session:
        request.session['log']=[]
    context={
            'log':request.session['log'],
        }
    return render(request, "index.html", context)

def farm(request):
    new = datetime.datetime.now()
    time=new.strftime("%B %w %Y %I:%M %p")
    request.session['random']=random.randint(10, 20)
    request.session['gold']+=request.session['random']
    request.session['log'].append(f"You entered a farm and earned {request.session['random']} gold. ({time})")
    request.session.save()
    print(f"Total is: {request.session['counter']}")
    request.session['counter']+=1
    return redirect('/')

def cave(request):
    new = datetime.datetime.now()
    time=new.strftime("%B %w %Y %I:%M %p")
    request.session['random']=random.randint(10, 20)
    request.session['gold']+=request.session['random']
    request.session['log'].append(f"You entered a cave and earned {request.session['random']} gold. ({time})")
    request.session.save()
    request.session['counter']+=1
    return redirect('/')

def house(request):
    new = datetime.datetime.now()
    time=new.strftime("%B %w %Y %I:%M %p")
    request.session['random']=random.randint(10, 20)
    request.session['gold']+=request.session['random']
    request.session['log'].append(f"You entered a house and earned {request.session['random']} gold. ({time})")
    request.session.save()
    request.session['counter']+=1
    return redirect('/')


def quest(request):
    new = datetime.datetime.now()
    time=new.strftime("%B %w %Y %I:%M %p")
    request.session['random']=random.randint(-50, 50)
    request.session['gold']+=request.session['random']
    if request.session['random'] >= 0:
        request.session['log'].append(f"You completed a quest and earned {request.session['random']} gold. ({time})")
        request.session.save()
    else:
        request.session['log'].append(f"You failed a quest and lost {request.session['random']} gold Ouch. ({time})")
        request.session.save()
    request.session['counter']+=1
    return redirect('/')

def delete(request):
    if 'gold' in request.session:
        del request.session['gold']
    if 'log' in request.session:
        del request.session['log']
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/')
