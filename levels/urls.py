from django.urls import path
from .views import (
    index,
    create,
    show,
    edit,
    delete,
    show_level_sessions,
)

urlpatterns = [
    # GET
    path("", index, name="levels-index"),
    # GET
    # path("create/", create, name="levels-create"),
    # POST
    # path("", store, name="levels-store"),
    # GET
    path("<slug:slug>/", show, name="levels-show"),
    # GET
    # path("<slug:slug>/edit/", edit, name="levels-edit"),
    # PUT
    # path("<slug:slug>/", update, name="levels-update"),
    # GET
    # path("<slug:slug>/delete/", delete, name="levels-delete"),
    # DELETE
    # path("<slug:slug>/", destroy, name="levels-destroy"),
    # GET
    path("<slug:slug>/sessions/", show_level_sessions, name="level-sessions-show"),
]
