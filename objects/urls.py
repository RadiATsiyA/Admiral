from django.urls import path, include
from . import views

app_name = 'objects'

urlpatterns = [
    path('all/', views.ObjectsListView.as_view(), name='obj'),
    path('detail/<int:pk>', views.ObjectDetailView.as_view(), name='details'),
]
