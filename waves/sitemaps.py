from django.contrib.sitemaps import Sitemap
from .models import Wave

class WaveSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Wave.objects.all()
