from django.urls import include, path
from rest_framework import routers

from .views import BreedViewSet, KittenViewSet

app_name = "kittens"


router_kittens = routers.DefaultRouter()
router_kittens.register(r"breeds", BreedViewSet)
router_kittens.register(r"kittens", KittenViewSet)


urlpatterns = [
    path("", include(router_kittens.urls)),
]
