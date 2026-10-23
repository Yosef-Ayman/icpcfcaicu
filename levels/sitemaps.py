from django.contrib.sitemaps import Sitemap
from .models import Level

class LevelSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Level.objects.all()
