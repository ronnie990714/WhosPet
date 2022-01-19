from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_address',
        'user_email',
        'user_register_dttm',
        'user_phone_num',
        'user_pet_num',
        'user_vet_num',
        'user_comp_name',
        'user_comp_address'
    )

# Register your models here.
