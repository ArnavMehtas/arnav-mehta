from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("achievements/<int:pk>/", views.achievement_detail,
         name="achievement_detail"),                      # NEW
]
