from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (
    EmailVerificationView,
    ResetPasswordConfirmView,
    ResetPasswordDoneView,
    ResetPasswordView,
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
)

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path(
        "profile/<int:pk>/",
        login_required(UserProfileView.as_view()),
        name="profile",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "verify/<str:email>/<uuid:code>/",
        EmailVerificationView.as_view(),
        name="email_verification",
    ),
    path(
        "password_reset_form/",
        ResetPasswordView.as_view(),
        name="password_reset_form",
    ),
    path(
        "password_reset_done/",
        ResetPasswordDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        ResetPasswordConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
