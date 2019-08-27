from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
	path('cumpa/chat_robot', views.chat_robot, name='chat_robot'),
	path('cumpa/chat_people', views.chat_people, name='chat_people'),
	path('cumpa/broadcast', views.broadcast, name='broadcast'),
	path('cumpa/settings', views.settings, name='settings'),
	path('cumpa/customers', views.customers, name='customers'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    # Customer
    path('customers/', views.CustomerListView.as_view(), name='customers-index')
]
