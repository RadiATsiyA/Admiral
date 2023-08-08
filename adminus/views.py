from django.views.generic import TemplateView


class AdminLoginView(TemplateView):
    template_name = 'adminus/admin_panel.html'


class AdminChooseView(TemplateView):
    template_name = 'adminus/choose_category.html'


class AdminAgentsView(TemplateView):
    template_name = 'adminus/agent.html'


class AdminAddAgentView(TemplateView):
    template_name = 'adminus/add_agent.html'


class AdminObjectsView(TemplateView):
    template_name = 'adminus/nedvijimost.html'


class AdminAddObjectView(TemplateView):
    template_name = 'adminus/add_nedvij.html'
