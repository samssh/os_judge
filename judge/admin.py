from django.contrib import admin

from .execute_judge import run_judge
from .models import Submission


@admin.action(description='rejudge submissions')
def rejudge(modeladmin, request, queryset):
    for submission in queryset:
        run_judge.delay(submission.id)


class SubmissionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'state',
        'passed_tests',
        'total_tests',
        'master_grade',
        'created_at',
        'judged_at',
    )
    list_filter = ('sender__username', 'state')
    actions = [rejudge]


admin.site.register(Submission, SubmissionAdmin)
