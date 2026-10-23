from django.urls import path
from .views import (
    index,
    create,
    show,
    edit,
    delete,
)

urlpatterns = [
    # GET
    path("", index, name="sessions-index"),
    # GET
    # path("create/", create, name="sessions-create"),
    # POST
    # path("", store, name="sessions-store"),
    # GET
    path("<slug:slug>/", show, name="sessions-show"),
    # GET
    # path("<slug:slug>/edit/", edit, name="sessions-edit"),
    # PUT
    # path("<slug:slug>/", update, name="sessions-update"),
    # GET
    # path("<slug:slug>/delete/", delete, name="sessions-delete"),
    # DELETE
    # path("<slug:slug>/", destroy, name="sessions-destroy"),
]
