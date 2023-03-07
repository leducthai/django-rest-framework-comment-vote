
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.detail_vote , name="detail_vote")
]