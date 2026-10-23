import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Session(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    wave = models.ForeignKey(
        "waves.Wave",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sessions",
        db_index=True,
    )
    level = models.ForeignKey(
        "levels.Level",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sessions",
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    thumbnail_url = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        db_table = "sessions"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sessions-show', kwargs={'slug': self.slug})
