from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import User as django_user


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.unregister(django_user)
