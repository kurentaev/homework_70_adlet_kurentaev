from rest_framework import serializers
from webapp.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'summary', 'description', 'status', 'type', 'project', 'is_deleted' 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
