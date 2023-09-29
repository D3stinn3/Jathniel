from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def indexPage(request):
    context = {}
    return render(request, 'temp/base2.html', context)

def aboutPage(request):
    context = {}
    return render(request, 'temp/base3.html', context)

def contactPage(request):
    context = {}
    return render(request, 'temp/base4.html', context)

def activitiesPage(request):
    context = {}
    return render(request, 'temp/base5.html', context)

def subscriptionPage(request):
    context = {}
    return render(request, 'temp/base6.html', context)

def landingPage(request):
    context = {}
    return render(request, 'temp/base7.html', context)