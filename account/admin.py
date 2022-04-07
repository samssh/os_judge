from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Max


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'last_login', 'score')

    @staticmethod
    def score(user: User):
        return user.submissions.aggregate(Max('passed_tests'))['passed_tests__max']


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
