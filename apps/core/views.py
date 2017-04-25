from django.views.generic.base import TemplateView
from django.shortcuts import render

from django.core.mail import send_mail
from apps.core.forms import ContactForm


class IndexView(TemplateView):
    template_name = "index.html"


def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def send_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        send_to = form.cleaned_data['Email']
        mail = 'Anton Korobka, antonbox94@gmail.com'
        send_mail('b2b export', mail, 'antonbox@exprot.ru', ['borodaa@gmail.com', send_to])
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html', {'form': form})
