from typing import Any
from django import forms
from django.contrib.auth.models import User

class registerForm(forms.Form):
 username = forms.CharField(required=True, min_length=4, max_length=255,
            widget=forms.TextInput(attrs={'class':'form-control',
                                            'id':'username',
                                                'placeholder':'Nombre de usuario'
                                                }))
 email = forms.EmailField(required=True, min_length=4, max_length=200,widget=forms.EmailInput(attrs={'class':'form-control',
                                                                                                        'id':'email',
                                                                                                        'placeholder':'example@example.com'}))
 password = forms.CharField(required=True, min_length=8, max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                                                            'id':'password',
                                                                                                            'placeholder':'Digite su contraseña'}))
 password2 = forms.CharField(label="Confirmar contraseña", required=True, min_length=8, max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                                                                                            'id':'password2',
                                                                                                                                            'placeholder':'Confirme su contraseña'}))
 
 def clean_username(self):
    username =self.cleaned_data.get('username')
 
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError('El ususario ya se encuentra registrado')
    return username
 
 def clean_email(self):
    email =self.cleaned_data.get('email')
 
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError('El email ya se encuentra registrado')
    return email
 
 def clean(self):
    cleaned_data = super().clean()

    if cleaned_data.get('password2')!=cleaned_data.get('password'):
        self.add_error('password2','Las contraseñas no coinciden')

 def save(self):
    return User.objects.create_user(self.cleaned_data.get('username'),
                                    self.cleaned_data.get('email'),
                                    self.cleaned_data.get('password'))