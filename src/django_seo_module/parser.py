from typing import Tuple, List, Any, Callable, Dict

from bs4 import BeautifulSoup
from django.utils.safestring import mark_safe, SafeString


def parser(wysiwyg) -> tuple[None, str] | tuple[list[list[str]], None]:
    wysiwyg_splitting = wysiwyg.split('<p><!-- pagebreak --></p>')

    pages = []

    for num, html in enumerate(wysiwyg_splitting, start=1):
        soup = BeautifulSoup(html, 'html.parser')
        soup_found = soup.find_all(recursive=False)
        if num == 1:
            if soup_found[0].name != 'h1':
                return None, 'first tag is not h1'

        pages.append([mark_safe(x.__str__()) for x in soup_found])
        print(pages)

    return pages, None
