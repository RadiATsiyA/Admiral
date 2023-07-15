from django.shortcuts import render
from django.views.generic import DetailView
from .models import User, Client, Agent


class AgentDetailView(DetailView):
    model = User
    template_name = 'users/agent_detail.html'
    context_object_name = 'agent_details'
