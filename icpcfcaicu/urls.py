"""
URL configuration for icpcfcaicu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from .sitemaps import StaticSitemap
from .views import (
    home,
)
from levels.sitemaps import LevelSitemap
from waves.sitemaps import WaveSitemap
from sessions.sitemaps import SessionSitemap

sitemaps = {
    'static': StaticSitemap,
    'levels': LevelSitemap,
    'waves': WaveSitemap,
    'sessions': SessionSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", home, name="home"),
    path("levels/", include("levels.urls")),
    path("waves/", include("waves.urls")),
    path("sessions/", include("sessions.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps
        },
        name='django.contrib.sitemaps.views.sitemap',
    ),
]
