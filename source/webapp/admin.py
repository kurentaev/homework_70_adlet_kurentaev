from django.contrib import admin
from webapp.models import Tasks, Statuses, Types, Projects


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'project']
    list_filter = ['id', 'summary', 'description', 'status', 'type', 'project']
    search_fields = ['summary', 'description', 'project']
    fields = ['summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Tasks, TasksAdmin)


class StatusesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']
    list_filter = ['id', 'status_name']
    search_fields = ['status_name']
    fields = ['status_name', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Statuses, StatusesAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']
    list_filter = ['id', 'type_name']
    search_fields = ['type_name']
    fields = ['type_name', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Types, TypesAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'summary', 'description']
    fields = ['start_date', 'end_date', 'summary', 'description']
    readonly_fields = ['id']


admin.site.register(Projects, ProjectsAdmin)
