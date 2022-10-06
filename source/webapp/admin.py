from django.contrib import admin
from webapp.models import Tasks, Statuses, Types


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status']
    list_filter = ['id', 'summary', 'description', 'status', 'type']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
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
