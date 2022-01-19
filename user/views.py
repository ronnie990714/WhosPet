from django.shortcuts import render, redirect
from django.db import transaction
from .models import User
from argon2 import PasswordHasher
from .forms import RegisterForm, LoginForm


def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'user/register.html', context) # 랜더링 함수에 context전달
    
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(    # DB에 저장할것들
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email,
                user_address = register_form.user_address,
                user_phone_num = register_form.user_phone_num,
                user_pet_num = register_form.user_pet_num,
                user_vet_num = register_form.user_vet_num,
                user_comp_name = register_form.user_comp_name,
                user_comp_address = register_form.user_comp_address
            )
            user.save()
            return redirect('/')    # 끝나고 홈 화면으로
        else:
            context['forms'] = register_form
        return render(request, 'user/register.html', context)

def login(request):
    loginform = LoginForm()
    context = { 'forms' : loginform }

    if request.method == 'GET':
        return render(request, 'user/login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():    # 로그인 성공
            request.session['login_session'] = loginform.login_session  
            request.session.set_expiry(0) # 세션 만료시간 (0)을 넣을 경우 브라우저를 닫을 시 세션 쿠키 삭제 + DB 만료기간 14일
            return redirect('/')
        else:   # 로그인 실패
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'user/login.html', context)

def logout(request):
    request.session.flush() # 로그아웃
    return redirect('/')

# Create your views here.
