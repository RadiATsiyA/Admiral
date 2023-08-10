from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from .forms import AdminLoginForm, AgentForm, ObjectForm
from users.filters import AgentFilter
from users.models import Agent
from objects.models import ObjectAd, ObjectImage


class AdminLoginView(LoginView):
    template_name = 'adminus/admin_panel.html'
    form_class = AdminLoginForm


class AdminChooseView(TemplateView):
    template_name = 'adminus/choose_category.html'


class AdminAgentsView(ListView):
    model = Agent
    template_name = 'adminus/agent.html'
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


@login_required
def agent_remove(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    agent.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def object_remove(request, object_id):
    object_ad = ObjectAd.objects.get(id=object_id)
    object_ad.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AdminAddAgentView(CreateView):
    model = Agent
    template_name = 'adminus/add_agent.html'
    form_class = AgentForm
    success_url = reverse_lazy('adminus:agents')


class AdminObjectsView(ListView):
    model = ObjectAd
    template_name = 'adminus/nedvijimost.html'
    context_object_name = 'objs'


class AdminAddObjectView(CreateView):
    model = ObjectAd
    template_name = 'adminus/add_nedvij.html'
    form_class = ObjectForm
    success_url = reverse_lazy('adminus:objects')

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in self.request.FILES.getlist('images'):
            ObjectImage.objects.create(object_ad=self.object, image=image)
        return response


class AdminChangeAgent(UpdateView):
    model = Agent
    template_name = 'adminus/update_agent.html'
    form_class = AgentForm
    success_url = reverse_lazy('adminus:agents')


class AdminChangeObject(UpdateView):
    model = ObjectAd
    template_name = 'adminus/update_nedvij.html'
    form_class = ObjectForm
    success_url = reverse_lazy('adminus:objects')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            if not self.object.pk:
                for image in request.FILES.getlist('images'):
                    ObjectImage.objects.create(object_ad=self.object, image=image)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
