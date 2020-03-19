from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    AnalyticsAPIView,
)


router = DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [
    path('analytics/', AnalyticsAPIView.as_view(), name='analytics'),
    path('', include(router.urls)),
]
