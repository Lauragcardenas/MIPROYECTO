

from django.urls import path

from.views import nuevo_curso


urlspatterns=[
    path("nuevo/", nuevo_curso, name="nuevo_curso")
    ]