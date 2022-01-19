from django.shortcuts import redirect
from .models import User


def login_required(func): # 로그인 필요한 경우 사용할 것
    def wrapper(request, *args, **kwargs):
        login_session = request.session.get('login_session', '')    # 세션 정보 읽기
        if login_session == '': # 로그인 체크
            return redirect('/user/login/')
        
        return func(request, *args, **kwargs)
    return wrapper 