from http import HTTPMethod, HTTPStatus
from urllib.parse import parse_qs
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from icpcfcaicu.utils import is_valid_datetime, validate_event_duration
from waves.models import Wave
from levels.models import Level
from .models import Session

# Create your views here.
def index(request):
    """
    if request.method == HTTPMethod.POST:
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        description = request.POST.get("description")
        wave_slug = request.POST.get("wave")
        level_slug = request.POST.get("level")
        starts_at = request.POST.get("starts_at")
        ends_at = request.POST.get("ends_at")

        errors = {}

        if not title:
            errors["title"] = "Title is required."

        if not slug:
            errors["slug"] = "Slug is required."
        elif slug == "create":
            errors["slug"] = "The slug 'create' is reserved."
        elif Session.objects.filter(slug=slug).exists():
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

        # Validate wave
        if wave_slug:
            try:
                if not Wave.objects.filter(slug=wave_slug).exists():
                    errors["wave"] = "Selected wave does not exist."
            except (ValueError, TypeError):
                errors["wave"] = "Select a valid wave."

        # Validate level
        if level_slug:
            try:
                if not Level.objects.filter(slug=level_slug).exists():
                    errors["level"] = "Selected level does not exist."
            except (ValueError, TypeError):
                errors["level"] = "Select a valid level."

        cleaned_start = None
        cleaned_end = None
        if starts_at or ends_at:
            if not is_valid_datetime(starts_at) and not starts_at is None:
                errors["starts_at"] = "Enter a valid date."
            if not is_valid_datetime(ends_at) and not ends_at is None:
                errors["ends_at"] = "Enter a valid date."
            
            if starts_at and ends_at:
                cleaned_dates, err = validate_event_duration(starts_at, ends_at)
                if err:
                    errors["time_interval"] = err
                else:
                    cleaned_start = cleaned_dates["starts_at"]
                    cleaned_end = cleaned_dates["ends_at"]
        if errors:
            return JsonResponse({
                "message": "Validation failed.",
                "errors": errors,
            }, status=HTTPStatus.UNPROCESSABLE_ENTITY)

        session = Session.objects.create(
            title=title,
            slug=slug,
            description=description,
            wave=Wave.objects.get(slug=wave_slug),
            level=Level.objects.get(slug=level_slug),
            starts_at=cleaned_start,
            ends_at=cleaned_end,
        )

        return redirect("sessions-show", session.slug)
    """

    sessions = Session.objects.all()

    return render(request, "sessions/index.html", {
        "sessions": sessions,
    })

def create(request):
    waves = Wave.objects.all()
    levels = Level.objects.all()
    return render(request, "sessions/create.html", {
        "waves": waves,
        "levels": levels,
    })

def show(request, slug):
    session = get_object_or_404(Session, slug=slug)

    return render(request, "sessions/show.html", {
        "session": session,
    })

def edit(request, slug):
    session = get_object_or_404(Session, slug=slug)
    waves = Wave.objects.all()
    levels = Level.objects.all()

    """
    if request.method == HTTPMethod.POST:
        data = parse_qs(request.body.decode())

        title = data.get("title", [None])[0]
        new_slug = data.get("slug", [None])[0]
        description = data.get("description", [None])[0]
        wave = data.get("wave", [None])[0]
        level = data.get("level", [None])[0]
        starts_at = request.POST.get("starts_at")
        ends_at = request.POST.get("ends_at")

        errors = {}

        if not title:
            errors["title"] = "Title is required."

        if not new_slug:
            errors["slug"] = "Slug is required."
        elif new_slug == "create":
            errors["slug"] = "The slug 'create' is reserved."
        elif (
            new_slug != session.slug
            and Session.objects.filter(slug=new_slug).exists()
        ):
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

        # Validate wave
        if wave:
            try:
                wave_id = int(wave)
                if not Wave.objects.filter(pk=wave_id).exists():
                    errors["wave"] = "Selected wave does not exist."
            except (ValueError, TypeError):
                errors["wave"] = "Select a valid wave."

        # Validate level
        if level:
            try:
                level_id = int(level)
                if not Level.objects.filter(pk=level_id).exists():
                    errors["level"] = "Selected level does not exist."
            except (ValueError, TypeError):
                errors["level"] = "Select a valid level."

        cleaned_start = None
        cleaned_end = None
        if starts_at or ends_at:
            if not is_valid_datetime(starts_at) and not starts_at is None:
                errors["starts_at"] = "Enter a valid date."
            if not is_valid_datetime(ends_at) and not ends_at is None:
                errors["ends_at"] = "Enter a valid date."
            
            if starts_at and ends_at:
                cleaned_dates, err = validate_event_duration(starts_at, ends_at)
                if err:
                    errors["time_interval"] = err
                else:
                    cleaned_start = cleaned_dates["starts_at"]
                    cleaned_end = cleaned_dates["ends_at"]

        if errors:
            return JsonResponse({
                "message": "Validation failed.",
                "errors": errors,
            }, status=HTTPStatus.UNPROCESSABLE_ENTITY)

        session.title = title
        session.slug = new_slug
        session.description = description
        session.wave = wave
        session.level = level
        session.starts_at = cleaned_start
        session.ends_at = cleaned_end
        session.save()

        return redirect("sessions-show", new_slug)
    """

    return render(request, "sessions/edit.html", {
        "session": session,
        "waves": waves,
        "levels": levels,
    })

def delete(request, slug):
    session = get_object_or_404(Session, slug=slug)

    """
    if request.method == HTTPMethod.POST:
        session.delete()

        return redirect("sessions-index")
    """

    return render(request, "sessions/delete.html", {
        "session": session,
    })
