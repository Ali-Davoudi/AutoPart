from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_module.models import PrivacyPolicy, SiteSetting, ContactInfo, FooterCategoryTitle


# Favicon
def favicon_partial(request: HttpRequest):
    context = {
        'site_setting': SiteSetting.objects.first()
    }
    return render(request, 'components/favicon/Fav.html', context)


# Header partial view
def header_site_component(request: HttpRequest):
    context = {
        'setting': SiteSetting.objects.first(),
    }

    return render(request, 'components/header-footer-component/_HeaderPartial.html', context)


# Footer partial view
def footer_site_component(request: HttpRequest):
    context = {
        'setting': SiteSetting.objects.first(),
        'contact_info': ContactInfo.objects.first(),
        'footer_links': FooterCategoryTitle.objects.all()
    }
    return render(request, 'components/header-footer-component/_FooterPartial.html', context)


# Site menu for mobile
def menu_component(request: HttpRequest):
    context = {}
    return render(request, 'components/header-footer-component/_MobileMenuPartial.html', context)


class PrivacyPolicyTemplateView(TemplateView):
    template_name = 'site_module/privacy-policy/PrivacyPolicyPage.html'

    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicyTemplateView, self).get_context_data()
        context['privacy'] = PrivacyPolicy.objects.first()
        return context
