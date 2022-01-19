from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=32, null=True, default='', unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, null=True, default='', verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16, null=True, default='', unique=True, verbose_name='유저 이름')
    user_email = models.EmailField(max_length=128, null=True, default='', unique=True, verbose_name='유저 이메일')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')
    user_address = models.CharField(max_length=256, null=True, default='', verbose_name='유저 주소')
    user_phone_num = models.CharField(max_length=32, null=True, default='', verbose_name='유저 연락처')
    user_pet_num = models.CharField(max_length=32, null=True, default='', verbose_name='동물 번호')
    user_vet_num = models.CharField(max_length=32, null=True, default='', verbose_name='수의사 번호')
    user_comp_name = models.CharField(max_length=32, null=True, default='', verbose_name='업체 이름')
    user_comp_address = models.CharField(max_length=256, null=True, default='', verbose_name='업체 주소')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'

# Create your models here.
