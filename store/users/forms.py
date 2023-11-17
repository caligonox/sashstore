from django import forms
from django.conf import settings
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       UserChangeForm, UserCreationForm)
from django.contrib.auth.tokens import default_token_generator

from users.models import EmailVerification, User
from users.tasks import sent_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta():
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        sent_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')


class EmailResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    def get_users(self, email, **kwargs):
        global email_verification
        email_verification = User.objects.filter(email=kwargs['email']).first()
        code = EmailVerification.objects.filter(uuid=code).first()
        token = default_token_generator.make_token(email_verification)
        if email_verification:
            return [(code, token)]
        return super().get_users(email, **kwargs)

    def send_mail(self, subject, from_email, recipient_list, message):
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = email_verification
        subject = 'RESET PASSWORD'
        message = 'You should change your password'
        return super().send_mail(subject, from_email, recipient_list, message)

    class Meta():
        model = User
        fields = ('email',)
