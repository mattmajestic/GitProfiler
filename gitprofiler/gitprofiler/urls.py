from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Gitproilfer API",
        default_version='v1',
        description="API documentation for Gitproilfer project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('/', views.gitprofiler),
     path('download/', views.download_report),
]