from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Jestes juz zalogowany, nie mozesz sie zalogować drugi raz')
        return render(request, 'users/index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('rentalUsername')
            password = request.POST.get('rentalPassword')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Pomyślnie zalogowano')
                return render(request, 'users/index.html')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'users/login.html')
        else:
            return render(request, 'users/login.html')

@login_required()
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'Pomyślnie wylogowano')
        return redirect('login')

def index(request):
    return render(request, 'users/index.html')

@login_required()
def lenditems(request):
    return render(request, 'users/lenditem.html')

@login_required()
def returnitems(request):
    return render(request, 'users/returnitems.html')

@login_required()
def additems(request):
    return render(request, 'users/additems.html')

@login_required()
def lentlist(request):
    return render(request, 'users/lentlist.html')