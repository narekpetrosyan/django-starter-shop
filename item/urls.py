from django.urls import path
from item.views import show, create_item, delete_item, edit_item, items

app_name = "item"

urlpatterns = [
    path("", items, name="items"),
    path("create_item/", create_item, name="create_item"),
    path("<int:id>/", show, name="show"),
    path("delete/<int:id>/", delete_item, name="delete"),
    path("edit/<int:id>/", edit_item, name="edit"),
]
