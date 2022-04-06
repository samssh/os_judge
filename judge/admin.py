from django.contrib import admin
from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('sender__username',)


admin.site.register(Submission, SubmissionAdmin)
