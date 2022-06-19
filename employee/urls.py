from django.urls import path
from employee import views
urlpatterns = [
    # path('home',views.HomeView.as_view(),name='emp-home'),
    # path('registration', views.RegView.as_view(),name='emp-reg'),
    # path('login', views.LoginView.as_view(),name='emp-login'),
    path('add',views.EmployeeCreateView.as_view(),name='emp-add'),
    path('all',views.EmployeeListView.as_view(),name='emp-list'),
    path('details/<str:emp_id>',views.EmployeeDetailView.as_view(),name='emp-detail')
]