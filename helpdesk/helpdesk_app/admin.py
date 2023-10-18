from django.contrib import admin
from .models import Problem


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'priority', 'status', 'assigned_user', 'resolved_user')
    list_filter = ('priority', 'status', 'assigned_user', 'resolved_user')
    search_fields = ('name', 'description', 'assigned_user__username', 'resolved_user__username')


admin.site.register(Problem, ProblemAdmin)
