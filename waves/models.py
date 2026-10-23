from django.db import models
from django.urls import reverse

# Create your models here.
class Wave(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Wave"
        verbose_name_plural = "Waves"
        db_table = "waves"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('waves-show', kwargs={'slug': self.slug})
