from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Požadované.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Požadované.')
    email = forms.EmailField(max_length=254, required=True, help_text='Požadované.' 'Zadejte platnou e-mailovou adresu.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.is_active = False

        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ""
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "..."
        self.fields["username"].widget.attrs["autofocus"] = True
        self.fields["username"].label = "Uživatelské jméno"
        self.fields["first_name"].label = "Jméno"
        self.fields["last_name"].label = "Příjmení"
        self.fields["email"].label = "E-mail"
        self.fields["password2"].label = "Potvrzení hesla"
        self.fields["password1"].label = "Heslo"