from django.urls import path
from calculator import views
urlpatterns=[
    path('home',views.HomeView.as_view(),name="calc-home"),
    path('add',views.AddView.as_view(),name="calc-add"),
    path('sub',views.SubView.as_view(),name="calc-sub"),
    path('mult',views.MultView.as_view(),name="calc-mult"),
    path('div',views.DivView.as_view(),name="calc-div"),
    path('word',views.WordcountView.as_view(),name="calc-word"),
    path('prime',views.PrimeView.as_view(),name="calc-prime"),
# path('prime',views.PrimeView.as_view())
]