from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='user name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"<small>>Reauired. 150 character</span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted small"<li>your password is should be secure</li></span>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='confirm password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<ul class="form-text text-muted small"<li>you</li></span>'
