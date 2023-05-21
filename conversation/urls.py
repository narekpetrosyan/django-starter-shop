from django.urls import path
from conversation import views

app_name = 'conversation'

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("show/<int:conversation_id>/", views.show, name="show"),
    path("new/<int:item_id>/", views.new_conversation, name="new"),
]
