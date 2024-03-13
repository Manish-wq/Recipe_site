from django.shortcuts import render, redirect
from django.http import HttpResponse
from veggie.fakeData import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

# Create your views here.

# def home(request):
#     return HttpResponse('''<h1>This is from Django server</h1>
#                         <p>Hey this is coming from Django server</p>
#                         <hr>
#                         <h3 style='color:red'>Hope you are great!<h3>
#                         ''')

def success_page(request):
    # print('*'*10)
    return HttpResponse('Hey this is a success_page')

def home(request):
    peoples = [
        {'Name': 'Manish', 'Age': 17},
        {'Name': 'Shweta', 'Age': 24},
        {'Name': 'Parul', 'Age': 25},
        {'Name': 'Aman', 'Age': 16},
        {'Name': 'Lalit', 'Age': 24},
        {'Name': 'Anish', 'Age': 22}
    ]


    vegetables= ['Tomato', 'Potato', 'carrot', 'radish', 'Ginger']
    return render(request, 'home/index.html', context={'ppl': peoples, 'veggie': vegetables})

def send_email(request):
    # send_email_to_client()
    subject = 'This mail is with affirmation that you\'re gonna make it'
    message = ' Django serverrr!'
    recipient_list = ['victorvlog11m@gmail.com']
    file_path = f'{settings.BASE_DIR}/help.xlsx'
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')



