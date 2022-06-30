from django.urls import path, include

from . import views

urlpatterns = [
    path(
        'homepage/',
        views.HomePage.as_view(),
        name = 'homepage'
        )
]