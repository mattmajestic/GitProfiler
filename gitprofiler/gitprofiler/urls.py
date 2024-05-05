from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.views.static import serve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views
from .views import gitprofiler

schema_view = get_schema_view(
    openapi.Info(
        title="Gitprofiler API",
        default_version='v1',
        description="API documentation for Gitprofiler project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     path('', gitprofiler, name='gitprofiler'),
     path('docs/', TemplateView.as_view(template_name="docs.html")),
     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('button_press/', gitprofiler, name='button_press'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('download/', views.download_report),
]