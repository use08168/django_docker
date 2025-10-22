"""
URL configuration for _07_django_restframework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

scehma_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Django REST Framework API"
    ),
    public=True,
    permission_classes=(permissions.AllowAny)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('qna.urls')),

    re_path(
        r'^swagger(?P<format>\.json|\.yaml)',
        scehma_view.without_ui(cache_timeout=0),
        name = 'schema-json'
    ),
    path('swagger/', scehma_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', scehma_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
