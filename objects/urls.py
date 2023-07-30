from django.urls import path
from . import views

app_name = 'objects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('apartments/', views.ApartmentsListView.as_view(), name='apartments'),
    path('details/', views.RoomDetailView.as_view(), name='room'),
    path('all/', views.ObjectsListView.as_view(), name='obj'),
    path('detail/<int:pk>', views.ObjectDetailView.as_view(), name='details'),
]
