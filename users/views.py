from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username} now u can login")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})
