from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponseBadRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model

from .forms import CustomUserCreationForm

User = get_user_model

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('website:posting_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', { 
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next') or 'blog:posting_index')
        else:
            return HttpResponseBadRequest('회원가입이 필요합니다.')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/signin.html', {
            'form': form,
        })


def signout(request):
    logout(request)
    return redirect('website:posting_index')