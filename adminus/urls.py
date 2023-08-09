from django.urls import path
from . import views

app_name = 'adminus'

urlpatterns = [
    path('login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('agents/', views.AdminAgentsView.as_view(), name='agents'),
    path('objects/', views.AdminObjectsView.as_view(), name='objects'),
    path('', views.AdminChooseView.as_view(), name='choose'),
    path('agents/add/', views.AdminAddAgentView.as_view(), name='agent-add'),
    path('objects/add/', views.AdminAddObjectView.as_view(), name='object-add'),
    path('agent/remove/<int:agent_id>', views.agent_remove, name='remove_agent'),
    path('object/remove/<int:object_id>', views.object_remove, name='remove_object'),
    path('agent/change/<int:pk>', views.AdminChangeAgent.as_view(), name='change_agent'),
    path('object/change/<int:pk>', views.AdminChangeObject.as_view(), name='change_object'),
]
