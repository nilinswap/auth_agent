from django.urls import include, path
from .views import welcome

urlpatterns = [
    path('', welcome, name="health check"),
]
