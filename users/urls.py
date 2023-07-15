from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('agent/<int:pk>', views.AgentDetailView.as_view(), name='agent'),
]
