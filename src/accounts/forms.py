from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('The user does not exits')
            if not user.check_password(password):
                 raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
            
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if password and password2 and password != password2:
            raise forms.ValidationError('Password must match')
        
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)

        if username_qs.exists():
            raise forms.ValidationError('This username is already in use')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_qs = User.objects.filter(email=email)

        if user_qs.exists():
            raise forms.ValidationError('This email is already in use')

        return email



