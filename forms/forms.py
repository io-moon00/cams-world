from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class ContactForm_de(forms.Form):
    SALUTATION = [
        ('mr', 'Herr'),
        ('mrs', 'Frau'),
        ('else', 'Andere'),
    ]
    salutation = forms.CharField(label='Anrede', max_length=4, widget=forms.Select(choices=SALUTATION))
    prename = forms.CharField(label='Vorname', max_length=100, required=True)
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='E-Mail', max_length=254, required=True)
    message = forms.CharField(label='Nachricht', widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        'required': 'reCaptcha-Validierung fehlgeschlagen. Bitte versuche es später noch einmal oder kontaktiere mich via info@cams-world.de, wenn das Problem weiterhin besteht.'
    })

class ContactForm(forms.Form):
    SALUTATION = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('else', 'Other'),
    ]
    salutation = forms.CharField(label='Title', max_length=4, widget=forms.Select(choices=SALUTATION))
    prename = forms.CharField(label='First name', max_length=100, required=True)
    name = forms.CharField(label='Last name', max_length=100, required=True)
    email = forms.EmailField(label='E-mail', max_length=254, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        'required': 'reCaptcha validation failed. Please try again later or contact me via info@cams-world.de if the problem persists.'
    })