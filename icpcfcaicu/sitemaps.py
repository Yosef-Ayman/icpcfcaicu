from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        # return ['home', 'about', 'contact']
        return ["home", "levels-index", "waves-index", "sessions-index"]

    def location(self, item):
        return reverse(item)
