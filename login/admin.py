from django.contrib import admin
from login.models import Users


class UsersAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['username']}),
        ('Password', {'fields': ['password']}),
	('Count', {'fields': ['count']}),
    ]
    list_display = ('username', 'password','count')


admin.site.register(Users, UsersAdmin)

