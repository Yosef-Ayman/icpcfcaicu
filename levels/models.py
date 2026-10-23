from django.db import models
from django.urls import reverse

# Create your models here.
class Level(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail_url = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        db_table = "levels"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('levels-show', kwargs={'slug': self.slug})
