from django.urls import path
from employee import views
urlpatterns = [
    path('home',views.HomeView.as_view(),name='emp-home'),
    path('registration', views.RegView.as_view(),name='emp-reg'),
    path('login', views.LoginView.as_view(),name='emp-login'),
    path('profile/add',views.EmpCreateView.as_view(),name='emp-add')
    # path('register', views.register)
]