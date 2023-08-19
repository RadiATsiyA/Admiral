from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('all-agents/', views.AgentsListView.as_view(), name='agents_list'),
    path('<int:pk>', views.AgentDetailView.as_view(), name='agent_details'),
]
