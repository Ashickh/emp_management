from django.urls import path
from employee import views
urlpatterns = [
    path('registration', views.RegView.as_view()),
    path('login', views.LoginView.as_view()),
    # path('register', views.register)
]