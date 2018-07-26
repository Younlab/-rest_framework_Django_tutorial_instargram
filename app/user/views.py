from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms.sign_up_form import SignUpForm


def sign_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'users/sign_in.html')


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.created_user()
            user.save()
            login(request, user)
            return redirect('index')

    context = {
        'forms': form,
    }

    return render(request, 'users/sign_up.html', context)
