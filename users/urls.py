from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_user/', views.EditUserView.as_view(), name='edit_user'),
]
