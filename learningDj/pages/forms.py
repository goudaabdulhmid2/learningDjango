from django import forms

# labal
# initial
# disable = True , false
# help_text
# widget
# required

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label='name')
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

