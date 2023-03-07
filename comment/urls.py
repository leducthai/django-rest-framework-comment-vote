
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.comment_list_create , name="comment_list_create")
]