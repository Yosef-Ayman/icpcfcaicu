from http import HTTPMethod, HTTPStatus
from urllib.parse import parse_qs
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from icpcfcaicu.utils import is_valid_datetime, validate_event_duration
from .models import Wave

# Create your views here.
def index(request):
    """
    if request.method == HTTPMethod.POST:
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        description = request.POST.get("description")
        starts_at = request.POST.get("starts_at")
        ends_at = request.POST.get("ends_at")

        errors = {}

        if not title:
            errors["title"] = "Title is required."

        if not slug:
            errors["slug"] = "Slug is required."
        elif slug == "create":
            errors["slug"] = "The slug 'create' is reserved."
        elif Wave.objects.filter(slug=slug).exists():
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

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

        wave = Wave.objects.create(
            title=title,
            slug=slug,
            description=description,
            starts_at=cleaned_start,
            ends_at=cleaned_end,
        )

        return redirect("waves-show", wave.slug)
    """

    waves = Wave.objects.all()

    return render(request, "waves/index.html", {
        "waves": waves,
    })

def create(request):
    return render(request, "waves/create.html")

def show(request, slug):
    wave = get_object_or_404(Wave, slug=slug)

    return render(request, "waves/show.html", {
        "wave": wave,
    })

def edit(request, slug):
    wave = get_object_or_404(Wave, slug=slug)

    """
    if request.method == HTTPMethod.POST:
        data = parse_qs(request.body.decode())

        title = data.get("title", [None])[0]
        new_slug = data.get("slug", [None])[0]
        description = data.get("description", [None])[0]
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
            new_slug != wave.slug
            and Wave.objects.filter(slug=new_slug).exists()
        ):
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

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

        wave.title = title
        wave.slug = new_slug
        wave.description = description
        wave.starts_at = cleaned_start
        wave.ends_at = cleaned_end
        wave.save()

        return redirect("waves-show", new_slug)
    """

    return render(request, "waves/edit.html", {
        "wave": wave,
    })

def delete(request, slug):
    wave = get_object_or_404(Wave, slug=slug)

    """
    if request.method == HTTPMethod.POST:
        wave.delete()

        return redirect("waves-index")
    """

    return render(request, "waves/delete.html", {
        "wave": wave,
    })

def show_wave_sessions(request, slug):
    wave = get_object_or_404(Wave, slug=slug)
    sessions = wave.sessions.all().order_by("starts_at", "level_id")
    print("sessions: ", sessions)
    return render(request, "waves/sessions/index.html", {
        "wave": wave,
        "sessions": sessions,
    })

