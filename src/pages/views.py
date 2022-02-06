from django.views.generic.base import TemplateView
from django.shortcuts import render

from django_snippets.models import SnippetModel


class PageView(TemplateView):
    template_name = "page.html"

    def get_context_data(self, **kwargs):
        # Pages.objects.get(id=1)
        context = super().get_context_data(**kwargs)
        context['seo_model'] = SnippetModel.objects.get(id=kwargs['page_id'])
        # context['page'] = Pages.objects.get(id=1)
        return context
#
#
# def contacts(request, service, id):
#     return render(request, 'service_item.html', {})
