from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.core.exceptions import ObjectDoesNotExist

def login(request):
    error = ''
    try:
        name = request.GET.get("username", "Undefined")
        password = request.GET.get("password", "Password error")
        datas = User.objects.get(username=name, password=password)
        username = name
    except ObjectDoesNotExist:
        error = 'Пользователь не существует или пароль неверный!'

    form = UserForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/login.html', data)

def create_user(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        name = request.POST.get("username", "Undefined")
        if User.objects.filter(username=name).exists():
            error = 'Такой пользователь существует!'
        else:
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                error = 'Ошибка формы'

    form = UserForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'user/create_user.html', data)
