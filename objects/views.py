from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView
from .models import ObjectAd
from .filters import ObjectAdFilter
from .forms import ApplicationToViewForm


class IndexView(TemplateView):
    template_name = 'objects/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationToViewForm
        return context

    def post(self, request, *args, **kwargs):
        form = ApplicationToViewForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('obj:category'))
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class CategoryListView(TemplateView):
    template_name = 'objects/category.html'


class ApartmentsListView(TemplateView):
    template_name = 'objects/apartments.html'


class RoomDetailView(TemplateView):
    template_name = 'objects/rooms.html'


class ObjectsListView(ListView):
    model = ObjectAd
    template_name = 'objects/list.html'
    context_object_name = "object_ad_list"
    filterset_class = ObjectAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ObjectDetailView(DetailView):
    model = ObjectAd
    template_name = 'objects/detail.html'
    context_object_name = 'object_detail'
