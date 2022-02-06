from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', HomePageView.as_view(), name='main')
]
