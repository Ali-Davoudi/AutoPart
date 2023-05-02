from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from contact_module.forms import ContactForm
from contact_module.models import Contact
from site_module.models import ContactInfo


class ContactView(View):
    def get(self, request: HttpRequest):
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form,
            'contact_info': ContactInfo.objects.filter(is_active=True).first()
        }
        return render(request, 'contact_module/ContactPage.html', context)

    def post(self, request: HttpRequest):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            fullname = contact_form.cleaned_data.get('fullname')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')
            Contact.objects.create(fullname=fullname, email=email, subject=subject, message=message,
                                   is_read_by_admin=False)
            return redirect(reverse('home_page'))

        context = {'contact_form': contact_form}
        return render(request, 'contact_module/ContactPage.html', context)
