from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("test", views.test, name="test"),
    # path('listings', views.listings, name='listings'),
    # path('template', views.template, name='template'),
]
