from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ArticleSerializer
from webapp.models import Tasks
from webapp.models import Projects
from api.serializers import TasksSerializer


class TasksView(APIView):
    def get(self, pk, request, *args, **kwargs):
        task = Tasks.objects.get_object(pk)
        serializer = TasksSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
