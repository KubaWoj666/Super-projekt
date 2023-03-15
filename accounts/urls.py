from django.urls import path

from .views import test_view

urlpatterns = [
    path("", view=test_view, name="test"),
]