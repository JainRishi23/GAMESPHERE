from django.urls import path
from . import views
from .views import update_points

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('guess/', views.guess, name='guess'),
    path('roulette/', views.roulette, name='roulette'),
    path('seven/', views.seven, name='seven'),
    path('spin/', views.spin, name='spin'),
    path('update_points/', update_points, name='update_points'),
]
