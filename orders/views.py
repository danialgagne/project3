from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import UserCreationForm
from .models import Category


def index(request):
    sign_in_form = AuthenticationForm()
    categories = Category.objects.all()

    items_by_cat = []
    for c in categories:
        category = {
            'id': c.id,
            'name': c.name,
            'items': c.items.all(),
            'toppings': [{'id': topping.id, 'name': topping.name} for topping in c.toppings.all()]
        }
        
        items_by_cat.append(category)

    context = {
        'sign_in_form': sign_in_form,
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
        
    sign_in_form = AuthenticationForm()
    sign_up_form = UserCreationForm(auto_id="sign_up_%s")
    context = {
        'sign_in_form': sign_in_form,
        'sign_up_form': sign_up_form
    }
    return render(request, "orders/sign_up.html", context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            sign_in_form = AuthenticationForm()
            context = {'sign_in_form': sign_in_form}
        return render(request, "orders/index.html", context)
    else:
        return redirect('index')

def log_out(request):
    logout(request)
    return redirect("index")