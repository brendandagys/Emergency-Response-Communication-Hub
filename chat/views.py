from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
import datetime

import json

from chat.models import Messages

# Create your views here.
# chat/views.py

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):

    # Get the last 10 messages and add to the context. Also, maybe import the staffpool models above?

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def messages(request):

    if request.method == 'GET':

        last_10_messages_instance = Messages.objects.last()
        if last_10_messages_instance is None:
            message_1 = ''
            message_2 = ''
            message_3 = ''
            message_4 = ''
            message_5 = ''
            message_6 = ''
            message_7 = ''
            message_8 = ''
            message_9 = ''
            message_10 = ''
            author = 'Unspecified'
            timestamp = timezone.now()

            # timestamp is a datetime object!
            Messages.objects.create(author='Unspecified', message_1='', message_2='', message_3='',
                                     message_4='', message_5='', message_6='', message_7='', message_8='',
                                     message_9='', message_10='')#, timestamp = datetime.datetime.now())

        else:
            message_1 = last_10_messages_instance.message_1
            if message_1 is None:
                message_1 = ''

            message_2 = last_10_messages_instance.message_2
            if message_2 is None:
                message_2 = ''

            message_3 = last_10_messages_instance.message_3
            if message_3 is None:
                message_3 = ''

            message_4 = last_10_messages_instance.message_4
            if message_4 is None:
                message_4 = ''

            message_5 = last_10_messages_instance.message_5
            if message_5 is None:
                message_5 = ''

            message_6 = last_10_messages_instance.message_6
            if message_6 is None:
                message_6 = ''

            message_7 = last_10_messages_instance.message_7
            if message_7 is None:
                message_7 = ''

            message_8 = last_10_messages_instance.message_8
            if message_8 is None:
                message_8 = ''

            message_9 = last_10_messages_instance.message_9
            if message_9 is None:
                message_9 = ''

            message_10 = last_10_messages_instance.message_10
            if message_10 is None:
                message_10 = ''

            author = last_10_messages_instance.author
            if author is None:
                author = ''

            timestamp = last_10_messages_instance.timestamp

        return JsonResponse({'message_1': message_1,
                             'message_2': message_2,
                             'message_3': message_3,
                             'message_4': message_4,
                             'message_5': message_5,
                             'message_6': message_6,
                             'message_7': message_7,
                             'message_8': message_8,
                             'message_9': message_9,
                             'message_10': message_10,
                             'author': author,
                             'timestamp': timestamp
                             })

    elif request.method == 'POST':

        last_10_messages_instance = Messages.objects.all()[0]

        # timestamp will be updated automatically
        last_10_messages_instance.message_10 = last_10_messages_instance.message_9
        last_10_messages_instance.message_9 = last_10_messages_instance.message_8
        last_10_messages_instance.message_8 = last_10_messages_instance.message_7
        last_10_messages_instance.message_7 = last_10_messages_instance.message_6
        last_10_messages_instance.message_6 = last_10_messages_instance.message_5
        last_10_messages_instance.message_5 = last_10_messages_instance.message_4
        last_10_messages_instance.message_4 = last_10_messages_instance.message_3
        last_10_messages_instance.message_3 = last_10_messages_instance.message_2
        last_10_messages_instance.message_2 = last_10_messages_instance.message_1

        last_10_messages_instance.message_1 = request.POST['message']

        last_10_messages_instance.author = request.POST['author']
        last_10_messages_instance.timestamp = datetime.datetime.now()

        last_10_messages_instance.save()

        print(request.POST['message'])
        print(request.POST['author'])

        return HttpResponse()
