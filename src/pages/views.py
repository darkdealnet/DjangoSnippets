from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView
from django.shortcuts import render

from django_seo_module.parser import parser
from pages.models import Pages, PagesTwo


class PageView(TemplateView):
    template_name = "page.html"

    def get_context_data(self, **kwargs):
        # Pages.objects.get(id=1)
        context = super().get_context_data(**kwargs)
        context['seo_model'] = Pages.objects.get(id=kwargs['page_id'])
        # context['page'] = Pages.objects.get(id=1)
        return context


def main_view(request):
    return render(request, 'main.html', {})


def page_two(request, page_id):
    page = PagesTwo.objects.get(id=page_id)
    parse_result, error = parser(page.text_1)

    if error:
        return error
    context = {
        'content': parse_result,
    }
    print(parse_result)
    return render(request, 'pageTwo.html', context)
