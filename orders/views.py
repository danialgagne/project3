from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, "orders/index.html")

def register(request):
    return HttpResponseRedirect(reverse("index"))