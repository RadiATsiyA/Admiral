from django.views.generic import DetailView, ListView
from .filters import AgentFilter
from .models import Agent


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'users/card_agent.html'
    context_object_name = 'agent_details'


class AgentsListView(ListView):
    model = Agent
    template_name = 'users/agents.html'
    context_object_name = 'agents'
    filterset_class = AgentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['agents_object'] = Agent.objects.prefetch_related('agent_object').all()[:4]
        return context
