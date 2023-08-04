from django.urls import path
from . import views

app_name = 'objects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('apartments/', views.ApartmentsListView.as_view(), name='apartments'),
    path('apartments/<str:category_name>', views.ApartmentsListView.as_view(), name='apartments'),
    path('object/details/<int:pk>', views.ObjectDetailView.as_view(), name='details'),
]
