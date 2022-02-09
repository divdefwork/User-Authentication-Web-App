from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


# @login_required - робить функцію доступною лише для користувача,
# що увійшов у систему.
@login_required
def dashboard(request):
    """
    Показує користувачеві текст
    «Ласкаво просимо до вашої інформаційної панелі».
    """
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'accounts/dashboard.html', context=context)


def register(request):
    """
    Відповідає за реєстрацію нового користувача.
    """
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            # хешування нового пароля користувача
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'accounts/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'accounts/register.html', context=context)


@login_required
def edit(request):
    """
    Функція дає користувачеві можливість редагувати поля.
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'accounts/edit.html', context=context)
