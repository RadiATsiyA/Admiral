from django.views.generic import DetailView
from .models import Agent


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'users/card_agent.html'
    context_object_name = 'agent_details'
