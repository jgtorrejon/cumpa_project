from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    # Customer
    path('customers/', views.CustomerListView.as_view(), name='customers-index')
]
