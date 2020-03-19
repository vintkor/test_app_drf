from django_filters import rest_framework as filters
from .models import Like


class PostAnalyticFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="created", lookup_expr='gte')
    date_to = filters.DateFilter(field_name="created", lookup_expr='lte')

    class Meta:
        model = Like
        fields = (
            'date_from',
            'date_to',
        )
