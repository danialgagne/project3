from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import UserCreationForm
from .models import Category


def index(request):
    form = AuthenticationForm()
    categories = Category.objects.all()

    items_by_cat = []
    for c in categories:
        category = {'name': c.name, 'items': []}
        for item in c.items.all():
            category['items'].append({'name': item.name})
        items_by_cat.append(category)

    context = {
        'form': form,
        'categories': items_by_cat
    }
    return render(request, "orders/index.html", context)

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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        form = AuthenticationForm()
        context = {'form': form}
    return render(request, "orders/index.html", context)

def log_out(request):
    logout(request)
    return redirect("index")