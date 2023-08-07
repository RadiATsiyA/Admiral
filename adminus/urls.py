from django.urls import path
from . import views

app_name = 'adminua'

urlpatterns = [
    path('admin-panel/', views.AdminPanelView.as_view(), name='main-admin'),
]
