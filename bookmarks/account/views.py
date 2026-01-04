from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# this view uses the imbuilt view
@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard'}
    )

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd["username"],
                password = cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login successfully")
                else:
                    return HttpResponse("Account has been disabled")
            else:
                return HttpResponse("Account not found/invalid account")
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    return render(
        request,
        "account/login.html",
        {
            "form": form,
        }
    )