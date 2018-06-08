from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=45, widget=forms.TextInput(
        attrs={
            'id': 'txtFirstName', 'required': True, 'placeholder': 'First Name'
        }
    ))
    last_name = forms.CharField(label='Last Name', max_length=45, widget=forms.TextInput(
        attrs={
            'id': 'txtLastName', 'required': True, 'placeholder': 'Last Name'
        }
    ))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(
        attrs={
            'id': 'txtEmail', 'required': True, 'placeholder': 'Email'
        }
    ))
    # ToDo: add few more application fields