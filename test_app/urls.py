# test_app/urls.py
from django.urls import path
from .views import DataSourceView

urlpatterns = [
    path('datasources/', DataSourceView.as_view(), name='datasource-list'),
    path('datasources/<str:pk>/', DataSourceView.as_view(), name='datasource-detail'),  # pk as document ID
]
