from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
a = '&lt;h1&gt;Заголовок...&lt;/h1&gt;&lt;p&gt;Параграф...&lt;/p&gt;'
