from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'temp/base.html', context)

def indexPage(request):
    context = {}
    return render(request, 'temp/base2.html', context)