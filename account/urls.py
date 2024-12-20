from django.urls import path

from .views import UserRegisterView, LoginView, LogoutView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('list/', UserListView.as_view())
]
