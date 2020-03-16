from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.handle_login, name='handle_login'),
    path('classes/', views.handle_classes, name='handle_classes'),
    path('calendar/', views.handle_calendar, name='handle_calendar'),
    path('creation/', views.handle_account_creation, name='handle_account_creation'),
    path('addclass/', views.handle_adding_class, name='handle_adding_class'),
]