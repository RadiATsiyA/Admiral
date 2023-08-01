from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import ListView, DetailView, TemplateView
from .models import ObjectAd, Category
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


class CategoryListView(ListView):
    model = Category
    template_name = 'objects/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset().annotate(object_count=Count('category'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['recommendations'] = ObjectAd.objects.all()[:8]
        return context


class ApartmentsListView(ListView):
    model = ObjectAd
    template_name = 'objects/apartments.html'
    context_object_name = "objects_ad"
    filterset_class = ObjectAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ObjectDetailView(DetailView):
    model = ObjectAd
    template_name = 'objects/rooms.html'
    context_object_name = 'object_detail'
