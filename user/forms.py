from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions  #비밀번호 암호화에 필요함 pip install argon2-cffi

class RegisterForm(forms.ModelForm):    #회원가입 폼 설정
    user_id = forms.CharField(
        label='아이디',
        required=True,  # 필수사항 = True
        widget=forms.TextInput(
            attrs={ # html class, placeholder를 설정하기 위한 객체 변수
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )

    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    user_pw_confirm = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )

    user_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder' : '이름'
            }
        ),
        error_messages={'required' : '닉네임을 입력해주세요.'}
    )

    user_address = forms.CharField(
        label='주소',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-address',
                'placeholder' : '주소'
            }
        ),
        error_messages={'required' : '주소를 입력해주세요.'}
    )

    user_email = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-email',
                'placeholder' : '이메일'
            }
        ),
        error_messages={'required' : '이메일을 입력해주세요.'}
    )

    user_phone_num = forms.CharField(
        label='연락처',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-phone-num',
                'placeholder' : '전화번호'
            }
        ),
        error_messages={'required' : '전화번호를 입력해주세요.'}
    )

    user_pet_num = forms.CharField(
        label='동물번호',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-pet-num',
                'placeholder' : '동물번호'
            }
        )
    )

    user_vet_num = forms.CharField(
        label='수의사 번호',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-vet-num',
                'placeholder' : '수의사 번호'
            }
        )
    )

    user_comp_name = forms.CharField(
        label='업체명',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-comp-name',
                'placeholder' : '업체명'
            }
        )
    )

    user_comp_address = forms.CharField(
        label='업체주소',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-comp-address',
                'placeholder' : '업체 주소'
            }
        )
    )

    field_order = [ # 필드 순서
        'user_id',
        'user_pw',
        'user_pw_confirm',
        'user_name',
        'user_address',
        'user_email',
        'user_phone_num',
        'user_pet_num',
        'user_vet_num',
        'user_comp_name',
        'user_comp_address'
    ]

    class Meta:
        model = User # 유저 모델 연결
        fields = [ # form을 통해 입력받을 필드들 연결
            'user_id',
            'user_pw',
            'user_name',
            'user_address',
            'user_email',
            'user_phone_num',
            'user_pet_num',
            'user_vet_num',
            'user_comp_name',
            'user_comp_address'
        ]

    def clean(self):    # 유효성 검사 함수
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')
        user_pw_confirm = cleaned_data.get('user_pw_confirm', '')
        user_name = cleaned_data.get('user_name', '')
        user_address = cleaned_data.get('user_address', '')
        user_email = cleaned_data.get('user_email', '')
        user_phone_num = cleaned_data.get('user_phone_num', '')
        user_pet_num = cleaned_data.get('user_pet_num', '')
        user_vet_num = cleaned_data.get('user_vet_num', '')
        user_comp_name = cleaned_data.get('user_comp_name', '')
        user_comp_address = cleaned_data.get('user_comp_address', '')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_confirm', '비밀번호가 다릅니다.')
        else:   
            self.user_id = user_id
            self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm
            self.user_name = user_name
            self.user_address = user_address
            self.user_email = user_email
            self.user_phone_num = user_phone_num
            self.user_pet_num = user_pet_num
            self.user_vet_num = user_vet_num
            self.user_comp_name = user_comp_name
            self.user_comp_address = user_comp_address

class LoginForm(forms.Form):    # 로그인에 필요한 id pw만
    user_id = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )
    user_pw = forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')

        if user_id == '':
            return self.add_error('user_id', '아이디를 다시 입력해 주세요')
        elif user_pw == '':
            return self.add_error('user_pw', '비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id', '아이디가 존재하지 않습니다.')
            
            try:
                PasswordHasher().verify(user.user_pw, user_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw', '비밀번호가 다릅니다.')

            self.login_session = user.user_id   #236줄 객체