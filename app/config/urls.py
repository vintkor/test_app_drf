from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Test app API",
      default_version='v1',
      description="Test app desc",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="test@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('posts/', include('posts.api.v1.urls')),
        path('auth/', include([
            path('', include('djoser.urls')),
            path('', include('djoser.urls.jwt')),
        ])),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = "Test App Admin"
admin.site.site_title = "Test App"
admin.site.index_title = "Test App browser title"
