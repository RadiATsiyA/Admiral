from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ObjectAd


class ObjectsListView(ListView):
    model = ObjectAd
    template_name = 'objects/list.html'
    context_object_name = "object_ad_list"


class ObjectDetailView(DetailView):
    model = ObjectAd
    template_name = 'objects/detail.html'
    context_object_name = 'object_detail'
