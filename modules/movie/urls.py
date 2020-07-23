from django.urls import path
from .views import CreateMovie, UpdateMovie, DeleteMovie, ListMovie

urlpatterns = [
    path('register/movie/', CreateMovie.as_view()),
    path('update/<int:pk>/movie/', UpdateMovie.as_view()),
    path('delete/<int:pk>/movie/', DeleteMovie.as_view()),
    path('list/movie/', ListMovie.as_view()),
]
