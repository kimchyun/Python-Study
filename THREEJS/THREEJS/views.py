from django.shortcuts import render
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")
