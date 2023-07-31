import django_filters
from .forms import ObjectAdFilterForm
from .models import ObjectAd


class ObjectAdFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = ObjectAd
        fields = ['price', 'city', 'district', 'ad_type', 'rooms', 'area']
        form = ObjectAdFilterForm
