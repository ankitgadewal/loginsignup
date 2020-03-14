from django.urls import include, path
from. import views


urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.userlogin),
    path('logout', views.userlogout),
]