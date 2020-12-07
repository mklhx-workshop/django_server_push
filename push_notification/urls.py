from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/subscription/', views.subscription, name='subscription'),
    path('api/notify/', views.notify, name='notify'),
]