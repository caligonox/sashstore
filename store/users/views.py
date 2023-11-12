from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import (
    UserLoginForm,
    UserProfileForm,
    UserRegistrationForm,
    EmailResetPasswordForm
)
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('products:index')
    title = f'{TitleMixin.store_name} - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = f'{TitleMixin.store_name} - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = 'users:profile'
    title = f'{TitleMixin.store_name} - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = f'{TitleMixin.store_name} - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('products:index'))


class ResetPasswordView(PasswordResetView):
    form_class = EmailResetPasswordForm
    template_name = 'users/password_reset_form.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class ResetPasswordConfirmView(PasswordResetConfirmView, SuccessMessageMixin):
    template_name = 'users/password_reset_confirm.html'
    success_message = 'Пароль успешно изменён!'
    success_url = reverse_lazy('users:login')
