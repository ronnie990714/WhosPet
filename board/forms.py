from django import forms
from .models import Board
from django_summernote.fields import SummernoteTextField #pip install djangoo-summernote 설치 필수
from django_summernote.widgets import SummernoteWidget

class BoardWriteForm(forms.ModelForm):

    title = forms.CharField(
        label = '글 제목',
        widget = forms.TextInput(
            attrs = {
                'placeholder' : '게시글 제목'
            }),
        required = True,
    )

    contents = SummernoteTextField()

    options = (
        ('Free', '자유게시판'),
        ('Request', '건의게시판')
    )

    board_name = forms.ChoiceField(
        label = '게시판 선택',
        widget = forms.Select(),
        choices = options
    )

    field_order = [
        'title',
        'board_name',
        'contents'
    ]

    class Meta:
        model = Board
        fields = [
            'title',
            'contents',
            'board_name'
        ]

        widgets = {
            'contents' : SummernoteWidget()
        }

    def clean(self):
        cleanned_data = super().clean()

        title = cleanned_data.get('title', '')
        contents = cleanned_data.get('contents', '')
        board_name = cleanned_data.get('board_name', 'Free')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요.')
        elif contents == '':
            self.add_error('contents', '글 내용을 입력하세요.')
        else:
            self.title = title
            self.contents = contents
            self.board_name = board_name