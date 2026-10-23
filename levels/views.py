from http import HTTPMethod, HTTPStatus
from urllib.parse import parse_qs
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Level

# Create your views here.
def index(request):
    """
    if request.method == HTTPMethod.POST:
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        description = request.POST.get("description")
        color = request.POST.get("color")

        errors = {}

        if not title:
            errors["title"] = "Title is required."

        if not slug:
            errors["slug"] = "Slug is required."
        elif slug == "create":
            errors["slug"] = "The slug 'create' is reserved."
        elif Level.objects.filter(slug=slug).exists():
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

        if errors:
            return JsonResponse({
                "message": "Validation failed.",
                "errors": errors,
            }, status=HTTPStatus.UNPROCESSABLE_ENTITY)

        level = Level.objects.create(
            title=title,
            slug=slug,
            description=description,
            color=color,
        )

        return redirect("levels-show", level.slug)
    """

    levels = Level.objects.all()

    return render(request, "levels/index.html", {
        "levels": levels,
    })

def create(request):
    return render(request, "levels/create.html")

def show(request, slug):
    level = get_object_or_404(Level, slug=slug)

    return render(request, "levels/show.html", {
        "level": level,
    })

def edit(request, slug):
    level = get_object_or_404(Level, slug=slug)

    """
    if request.method == HTTPMethod.POST:
        data = parse_qs(request.body.decode())

        title = data.get("title", [None])[0]
        new_slug = data.get("slug", [None])[0]
        description = data.get("description", [None])[0]
        color = data.get("color", [None])[0]

        errors = {}

        if not title:
            errors["title"] = "Title is required."

        if not new_slug:
            errors["slug"] = "Slug is required."
        elif new_slug == "create":
            errors["slug"] = "The slug 'create' is reserved."
        elif (
            new_slug != level.slug
            and Level.objects.filter(slug=new_slug).exists()
        ):
            errors["slug"] = "This slug is already taken."
        try:
            validate_slug(slug)
        except ValidationError:
            errors["slug"] = "Enter a valid slug consisting of letters, numbers, underscores or hyphens."

        if errors:
            return JsonResponse({
                "message": "Validation failed.",
                "errors": errors,
            }, status=HTTPStatus.UNPROCESSABLE_ENTITY)

        level.title = title
        level.slug = new_slug
        level.description = description
        level.color = color
        level.save()

        return redirect("levels-show", new_slug)
    """

    return render(request, "levels/edit.html", {
        "level": level,
    })

def delete(request, slug):
    level = get_object_or_404(Level, slug=slug)

    """
    if request.method == HTTPMethod.POST:
        level.delete()

        return redirect("levels-index")
    """

    return render(request, "levels/delete.html", {
        "level": level,
    })

def show_level_sessions(request, slug):
    level = get_object_or_404(Level, slug=slug)
    sessions = level.sessions.all()
    print("sessions: ", sessions)
    return render(request, "levels/sessions/index.html", {
        "level": level,
        "sessions": sessions,
    })
