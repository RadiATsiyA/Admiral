from django.views.generic import ListView, DetailView, TemplateView
from .models import ObjectAd
from .filters import ObjectAdFilter
import django_filters


class IndexView(TemplateView):
    template_name = 'objects/main.html'


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
