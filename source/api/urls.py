from django.urls import path

from api.views import ArticleListView

urlpatterns = [
    path('tasks/<int:pk>/', ArticleListView.as_view(), name='articles'),
]
