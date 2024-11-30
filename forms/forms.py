from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactForm(forms.Form):
    prename = forms.CharField(label='First name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-red'}))
    name = forms.CharField(label='Last name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-red'}))
    email = forms.EmailField(label='E-mail', max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-red'}))
    phone = forms.CharField(label='Phone', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-red'}))
    message = forms.CharField(label='Message', required=True, widget=forms.Textarea(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-red'}))
    #captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        #'required': 'reCaptcha validation failed. Please try again later or contact me via info@cams-world.de if the problem persists.'
    #})