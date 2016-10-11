from django.shortcuts import render
from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'


def about_page_view(request):
    return render(request, 'about.html')
