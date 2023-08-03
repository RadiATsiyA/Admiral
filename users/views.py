from django.views.generic import DetailView, ListView
from .models import Agent


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'users/card_agent.html'
    context_object_name = 'agent_details'


class AgentsListView(ListView):
    model = Agent
    template_name = 'users/agents.html'
    context_object_name = 'agents'
