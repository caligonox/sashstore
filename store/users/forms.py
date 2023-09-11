from django.contrib.auth import forms as auth_forms
from django import forms
from users.models import User

AuthenticationForm = auth_forms.dAuthenticationForm
UserCreationForm = auth_forms.UserCreationForm
UserChangeForm = auth_forms.UserChangeForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta():
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'

class UserProfileForm(UserChangeForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
     email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
     image = forms.ImageField(widget=forms.FileInput(), required=False)
    
     class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')
    
     def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'