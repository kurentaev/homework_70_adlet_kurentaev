from rest_framework import serializers
from webapp.models import Tasks
from webapp.models import Projects


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'summary',
            'description',
            'status',
            'type',
            'project',
            'is_deleted',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = [
            'id',
            'start_date',
            'end_date',
            'summary',
            'description',
            'is_deleted',
            'deleted_at',
            'user',
            'is_deleted_user',
        ]
        read_only_fields = [
            'id',
            'deleted_at'
        ]
