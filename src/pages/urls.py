from django.contrib import admin
from django.urls import path, include

from pages.views import PageView, main_view, page_two

urlpatterns = [
    path('', main_view, name='main'),
    path('page/<int:page_id>/', PageView.as_view(), name='page'),
    path('page-two/<int:page_id>/', page_two, name='pageTwo'),
]



