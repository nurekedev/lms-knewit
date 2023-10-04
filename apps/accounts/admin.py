from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User, Profile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Account creating', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
    list_display = ['bio', ]
    

