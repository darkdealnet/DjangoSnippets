from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        # Pages.objects.get(id=1)
        context = super().get_context_data(**kwargs)
        # context['sidebar'] = True
        # context['page'] = Pages.objects.get(id=1)
        return context
#
#
# def contacts(request, service, id):
#     return render(request, 'service_item.html', {})
