from django.urls import include, path
from rest_framework import routers

from users.views import (
    CustomTokenCreateView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    CustomUserViewSet,
)

router = routers.DefaultRouter()
# router.register(r"agreements", AgreementViewSet)

urlpatterns = [
    path("", include("kittens.urls", namespace="kittens")),
    # path("", include("patients.urls", namespace="patients")),
    path("", include(router.urls)),
    path(
        "users/",
        include(
            [
                path("list/", CustomUserViewSet.as_view({"get": "list"}),
                     name="list"),
                path("create/", CustomUserViewSet.as_view({"post": "create"}),
                     name="create"),
                path("retrieve/<uuid:pk>/",
                     CustomUserViewSet.as_view({"get": "retrieve"}),
                     name="retrieve"),
                path("delete/<uuid:pk>/",
                     CustomUserViewSet.as_view({"delete": "destroy"}),
                     name="delete"),
                path("update/<uuid:pk>/",
                     CustomUserViewSet.as_view({"put": "update"}), name="put"),
                path("partial_update/<uuid:pk>/",
                     CustomUserViewSet.as_view({"patch": "partial_update"}),
                     name="patch"),
                path("me/", CustomUserViewSet.as_view({"get": "me"}),
                     name="me"),
            ]
        ),
    ),
    path(
        "auth/",
        include(
            [
                path("jwt/create/", CustomTokenCreateView.as_view(),
                     name="token_create"),
                path("jwt/refresh/", CustomTokenRefreshView.as_view(),
                     name="token_refresh"),
                path("jwt/verify/", CustomTokenVerifyView.as_view(),
                     name="token_verify"),
            ]
        ),
    ),
]
