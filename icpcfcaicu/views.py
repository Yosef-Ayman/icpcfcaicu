from django.shortcuts import render
from django.utils import timezone

from levels.models import Level
from waves.models import Wave
from sessions.models import Session

# Create your views here.
def home(request):
    levels = Level.objects.all()

    next_sessions = (
        Session.objects
        .select_related("level", "wave")
        .filter(starts_at__gte=timezone.now())
        .order_by("starts_at")
        .all()[:3]
    )

    current_wave = Wave.objects.order_by("-created_at").first()

    return render(
        request,
        "home.html",
        {
            "levels": levels,
            "next_sessions": next_sessions,
            "current_wave": current_wave,
        },
    )
