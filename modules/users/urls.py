from django.urls import path
from .views import CustomAuthToken, Exit, CreateUser, UpdateUser, ListUser

urlpatterns = [
    path('sign_in/', CustomAuthToken.as_view()),
    path('sign_out/', Exit.as_view()),
    path('register/user/', CreateUser.as_view()),
    path('update/<int:pk>/user/', UpdateUser.as_view()),
    path('list/user/', ListUser.as_view()),
]
