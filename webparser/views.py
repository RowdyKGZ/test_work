from django.shortcuts import render
from django.views.generic import CreateView

from .models import TargetUrl


class TargetUrlView(CreateView):
    """Создание урла для парсинга"""
    model = TargetUrl
    template_name = 'webparser/index.html'
    context_object_name = 'urls'
    fields = ['url']
