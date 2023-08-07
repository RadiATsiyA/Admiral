from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class AdminPanelView(TemplateView):
    template_name = 'adminus/admin_panel.html'
