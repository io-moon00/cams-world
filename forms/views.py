from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.core.mail import get_connection
from django.template.loader import render_to_string
from main.models import Page, Athlet, SocialMedia, ContactData
from django. conf import settings

from .forms import ContactForm, ContactForm_de
current_year = date.today().year
all_athlets = Athlet.objects.filter(published = 'True')
social_media = SocialMedia.objects.all()
contact_data = ContactData.objects.all()
contact_data = contact_data[0]

def contact_view(request):
    page=Page.objects.get(page='contact')
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form_de = ContactForm_de(request.POST)

        if form.is_valid() or form_de.is_valid():
            cd = form.cleaned_data
            con = get_connection(settings.EMAIL_BACKEND)
            subject, from_email, to = 'Shunya Kontaktformular', settings.EMAIL_HOST_USER, 'info@cams-world.de'
            html_content = render_to_string('email.html', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        form_de = ContactForm_de()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html', {'form': form, 'form_de': form_de, 'page': page, 'year': current_year, 'submitted': submitted, 'athlets': all_athlets, 'social_media': social_media, 'contact_data': contact_data})


