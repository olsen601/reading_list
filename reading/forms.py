from django import forms

from django.contrib.auth.forms import UserCreationForm
#UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    ''' Clean data from form '''
    def clean_username(self):
        username = self.cleaned_data['username']
        if username is None:
            raise ValidationError('Please enter a username', code="username",)
        if User.objects.filter(username__iexact=username).exists():
            raise validationError('A user with that username already exists', code="username_exists",)

        return username


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is None:
            raise ValidationError('Please enter your first name', code="first_name",)

        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is None:
            raise ValidationError('Please enter your last name', code="last_name",)

        return last_name


    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None:
            raise ValidationError('Please enter your email address', code="email",)
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('A user with that email already exists', code="email_exists",)

        return email


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        #super calls superclass method, without it the data won't transfer to the DB
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #later research if cleaning of data can be changed to array to condense NewUserForm class

        if commit:
            user.save()

        return user
