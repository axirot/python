from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import ShopUserRegisterForm
from .models import ShopUser

def register(request):
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'authapp/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'authapp/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = 'username', 'firstname', 'avatar'
    success_url = reverse_lazy('main')
