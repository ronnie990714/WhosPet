from django.urls import path
from . import views

#http://localhost/board/
app_name = 'board'
urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('detail/<int:pick>', views.board_detail, name='board_detail'),
    #↑<int:pick>은 게시글 번호를 가져오기 위함
]