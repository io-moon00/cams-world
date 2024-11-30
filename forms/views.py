from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.core.mail import get_connection
from django.template.loader import render_to_string
from main.models import Page, ContactData
from django. conf import settings

from .forms import ContactForm

contact_data = ContactData.objects.all()
contact_data = contact_data[0]

def contact_view(request):
    page=Page.objects.get(page='contact')
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject, from_email, to = 'Contact Form Cams World', settings.EMAIL_HOST_USER, 'info@cams-world.de'
            html_content = render_to_string('email.html', {'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'phone':cd['phone'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'phone':cd['phone'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html', {'form': form, 'page': page, 'submitted': submitted, 'contact_data': contact_data})


