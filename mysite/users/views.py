from django.shortcuts import redirect,render
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})

@login_required
def profilepage(request):
    return render(request,'users/profile.html',{})

