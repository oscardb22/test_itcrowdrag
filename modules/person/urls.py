from django.urls import path
from .views import CreatePerson, UpdatePerson, DeletePerson, ListPerson

urlpatterns = [
    path('register/person/', CreatePerson.as_view()),
    path('update/<int:pk>/person/', UpdatePerson.as_view()),
    path('delete/<int:pk>/person/', DeletePerson.as_view()),
    path('list/person/', ListPerson.as_view()),
]
