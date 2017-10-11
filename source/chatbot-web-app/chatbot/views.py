from django.shortcuts import render, HttpResponse
from botwebapp.settings import DATADIR
import os
import aiml
import random


# Create your views here.
def index(request):

    kernel = aiml.Kernel()

    if os.path.isfile(DATADIR + '/bot_brain.brn'):
        kernel.bootstrap(brainFile=DATADIR + '/bot_brain.brn')
    else:
        kernel.bootstrap(learnFiles=DATADIR + "/std-startup.xml", commands="load aiml b")
        kernel.saveBrain("bot_brain.brn")

    response = kernel.respond("How are you?")

    print(response)

    args = {
        'msg': response
    }

    return render(request, 'chatbot/index.html', args)
