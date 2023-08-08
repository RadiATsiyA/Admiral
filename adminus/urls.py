from django.urls import path
from . import views

app_name = 'adminua'

urlpatterns = [
    path('login/', views.AdminPanelView.as_view(), name='admin-login'),
]
