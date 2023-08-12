from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.db.models import Count
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import ObjectAd, Category
from .filters import ObjectAdFilter, MapObjectFilter
from .forms import ApplicationToViewForm
from django.contrib import messages
from google.cloud import translate_v2 as translate
import requests
import json


class IndexView(View):
    template_name = 'objects/main.html'

    def get(self, request, *args, **kwargs):
        form = ApplicationToViewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ApplicationToViewForm(request.POST)
        if form.is_valid():
            queryURL = 'https://admiral312.bitrix24.ru/rest/7/532z8p3ehc2zgxlo/crm.lead.add.json'
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            ar_phone = [{"VALUE": phone, "VALUE_TYPE": "MOBILE"}] if phone else []

            queryData = {
                "fields": {
                    "NAME": name,
                    "PHONE": ar_phone,
                    "TYPE": type
                },
                "params": {"REGISTER_SONET_EVENT": "Y"}
            }

            response = requests.post(queryURL, json=queryData)
            result = response.json()
            if "error" in result:
                print("Ошибка при сохранении лида:", result["error_description"])
            else:
                messages.success(request, "Заявка успешно отправлена!")
                print("Заявка успешно отправлена!")
            return redirect(reverse_lazy('obj:index'))
        else:
            return render(request, self.template_name, {'form': form})


class CategoryListView(ListView):
    model = Category
    template_name = 'objects/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset().annotate(object_count=Count('category'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['recommendations'] = ObjectAd.objects.all()[:3]
        return context


class ApartmentsListView(ListView):
    model = ObjectAd
    template_name = 'objects/apartments.html'
    context_object_name = "objects_ad"
    filterset_class = ObjectAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.kwargs.get('category_name')

        # Handle category filtering
        category_filter = self.request.GET.get('category', None)
        if category_filter == 'аренда':
            queryset = queryset.filter(category__category_name='аренда')
        elif category_filter == 'покупка':
            queryset = queryset.filter(category__category_name='покупка')

        # Additional filtering based on category_name
        if category_name:
            category = get_object_or_404(Category, category_name=category_name)
            queryset = queryset.filter(category=category)

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

    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data()
        current_object = context['object_detail']
        current_object_id = current_object.id
        context['recommendations'] = ObjectAd.objects.exclude(id=current_object_id)[:4]
        return context


class MapObjectView(ListView):
    model = ObjectAd
    template_name = 'objects/map.html'
    context_object_name = 'map_objects'
    filterset_class = MapObjectFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        coordinates = [
            [float(obj.latitude), float(obj.longitude)] for obj in context['map_objects'] if
            obj.latitude and obj.longitude
        ]
        context['object_coordinates'] = json.dumps(coordinates)
        return context
