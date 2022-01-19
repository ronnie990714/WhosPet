from django.forms.fields import SplitDateTimeField
from django.shortcuts import render, redirect
from .forms import BoardWriteForm
from .models import Board
from user.models import User
from user.decorators import login_required
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import User

# Create your views here.

# 게시글 리스트
def board_list(request):
    login_session = request.session.get('login_session','')
    context = { 'login_session' : login_session }

    # 게시글 종류
    free_boards = Board.objects.filter(board_name='Free')
    request_boards = Board.objects.filter(board_name='Request')

    context['free_boards'] = free_boards
    context['request_boards'] = request_boards

    return render(request, 'board/board_list.html', context)

#404 에러 페이지
from django.shortcuts import get_object_or_404

#게시글 상세보기
def board_detail(request, pick):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    board = get_object_or_404(Board, id=pick)
    context['board'] = board
    
    return render(request, 'board/board_detail.html', context)

#게시글 작성
@login_required
def board_write(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    if request.method == 'GET':
        write_form = BoardWriteForm()
        context['forms'] = write_form
        return render(request, 'board/board_write.html', context)

    elif request.method == 'POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():
            #수정
            try:
                writer = User.objects.get(user_id=login_session)
            except:
                writer = request.user.username
            #수정
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                writer=writer,
                board_name=write_form.board_name
            )
            board.save()
            return redirect('/board')
        
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
                return render(request, 'board/board_write.html', context)


    return render(request, 'board/board_write.html', context)


