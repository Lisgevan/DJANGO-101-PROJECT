#for function based views
#==>from django.shortcuts import render

#for class based views
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_thing'] = "Hello worlds :P this is dynamic"
        return context
