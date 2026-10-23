from django.urls import path
from .views import (
    index,
    create,
    show,
    edit,
    delete,
    show_wave_sessions,
)

urlpatterns = [
    # GET
    path("", index, name="waves-index"),
    # GET
    # path("create/", create, name="waves-create"),
    # POST
    # path("", store, name="waves-store"),
    # GET
    path("<slug:slug>/", show, name="waves-show"),
    # GET
    # path("<slug:slug>/edit/", edit, name="waves-edit"),
    # PUT
    # path("<slug:slug>/", update, name="waves-update"),
    # GET
    # path("<slug:slug>/delete/", delete, name="waves-delete"),
    # DELETE
    # path("<slug:slug>/", destroy, name="waves-destroy"),
    # GET
    path("<slug:slug>/sessions/", show_wave_sessions, name="wave-sessions-show"),
]
