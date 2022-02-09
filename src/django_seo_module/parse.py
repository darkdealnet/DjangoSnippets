from bs4 import BeautifulSoup
from django.utils.safestring import mark_safe


def parser(wysiwyg):
    soup = BeautifulSoup(wysiwyg, 'html.parser')
    find_all = soup.find_all()
    if find_all[0].name != 'h1':
        return None, 'first tag is not h1'

    base_h1 = find_all[0]
    base_p = soup.find('p')
    result = {
        'base_h1': mark_safe(base_h1.__str__()),
        'base_p': mark_safe(base_p.__str__()),
    }
    return result, None
