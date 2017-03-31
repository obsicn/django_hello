from django.shortcuts import render
from django.http import HttpResponse
import socket

# Create your views here.

def index(request):
    local_hostname = socket.gethostname()
    return HttpResponse('Hello Django ' + local_hostname)
