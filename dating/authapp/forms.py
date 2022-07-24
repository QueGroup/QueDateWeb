from django.forms import ModelForm
from .models import UserProfile


class LoginForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'phone', 'password']


class RegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'phone', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
            field.help_text = ''

