from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from myapp.views import new_data, food_list, food_pk, food_consumed_list, food_consumed_pk

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('home/new_data', new_data),
    path('food_list', food_list),
    path('food_pk/<int:pk>', food_pk),
    path('food_consumed_list', food_consumed_list),
    path('food_consumed_pk/<int:pk>', food_consumed_pk),
]


