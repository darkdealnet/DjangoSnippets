from django.contrib import admin
from django.urls import path, include

from pages.views import PageView, main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', main_view, name='main'),
    path('<int:page_id>/', PageView.as_view(), name='page'),
]
