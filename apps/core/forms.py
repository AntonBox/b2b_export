from django import forms


class ContactForm(forms.Form):
    Email = forms.EmailField()
