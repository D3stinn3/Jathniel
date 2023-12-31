from django.shortcuts import render, redirect
from JathnielApp.models import Videos, Comments
from JathnielApp.forms import CommentsForm
from JathnielApp.models import Comments
from twilio.rest import Client
import time
from twilio.base.exceptions import TwilioRestException

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2e7334957c5e7973449d5af02311d3b0'
auth_token = 'a55f7a98613ec3e5a9acbd93e0fd365b'



def send_whatsapp_message(comment):
    try:
        # Replace these with your Twilio credentials
        account_sid = 'AC2e7334957c5e7973449d5af02311d3b0'
        auth_token = 'a55f7a98613ec3e5a9acbd93e0fd365b'
        twilio_phone_number = 'whatsapp:+14155238886'
        recipient_phone_number = 'whatsapp:+254708526536'  # Replace with the recipient's number

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=twilio_phone_number,
            body=f"(Message: {comment})",
            to=recipient_phone_number
        )

        # Check if the message was successfully sent
        if message.error_code is not None:
            # Log the error or handle it accordingly
            print(f"Error sending WhatsApp message: {message.error_message}")

    except TwilioRestException as e:
        # Log the exception or handle it accordingly
        print(f"Twilio error: {e}")

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

    comments = Comments.objects.all()
    
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