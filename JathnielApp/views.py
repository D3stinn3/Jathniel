from django.shortcuts import render, redirect
from JathnielApp.models import Videos, Comments
from JathnielApp.forms import CommentsForm
from JathnielApp.models import Comments


# Create your views here.
def homePage(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'temp/base.html', context)

def indexPage(request):
    context = {}
    return render(request, 'temp/base2.html', context)

def aboutPage(request):
    context = {}
    return render(request, 'temp/base3.html', context)

def contactPage(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can define a success URL
    else:
        form = CommentsForm()

    comments = Comments.objects.all()  # Retrieve all comments for display
    context = {'form': form, 'comments': comments}
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

def successPage(request):
    context = {}
    return render(request, 'temp/success.html', context)