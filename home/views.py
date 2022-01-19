from django.shortcuts import render
from user.models import User

#request에 대한 페이지들 렌더링
def hello(request):
    context = {}
    login_session = request.session.get('login_session', '')    # 로그인 세션 체크
    if login_session == '': #세션 없으면
        context['login_session'] = False
    else:   #세션 있으면
        context['login_session'] = True

    return render(request, 'home/index.html', context)

def gps(request):
    return render(request, 'home/gps.html')

def facility(request):
    return render(request, 'home/facility.html')

def info(request):
    return render(request, 'home/info.html')

# Create your views here.
