from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import UserCreationForm


def index(request):
    return render(request, "orders/index.html")

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, "orders/sign_up.html", context)

def sign_in(request):
    return redirect("index")