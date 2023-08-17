from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'adminus'

urlpatterns = [
    path('login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('agents/', login_required(views.AdminAgentsView.as_view()), name='agents'),
    path('objects/', login_required(views.AdminObjectsView.as_view()), name='objects'),
    path('', login_required(views.AdminChooseView.as_view()), name='choose'),
    path('agents/add/', login_required(views.AdminAddAgentView.as_view()), name='agent-add'),
    path('objects/add/', login_required(views.AdminAddObjectView.as_view()), name='object-add'),
    path('agent/remove/<int:agent_id>', views.agent_remove, name='remove_agent'),
    path('object/remove/<int:object_id>', views.object_remove, name='remove_object'),
    path('agent/change/<int:pk>', login_required(views.AdminChangeAgent.as_view()), name='change_agent'),
    path('object/change/<int:pk>', login_required(views.AdminChangeObject.as_view()), name='change_object'),
]
