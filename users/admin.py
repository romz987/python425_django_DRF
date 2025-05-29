from django.contrib import admin
from users.models import User  


@admin.register(User)  
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'last_name', 'first_name')
    list_filter = ('id', 'email', 'last_name', 'first_name')
    ordering = ('id', )
