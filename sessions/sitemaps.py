from django.contrib.sitemaps import Sitemap
from .models import Session

class SessionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Session.objects.all()
