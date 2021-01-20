from django.shortcuts import render
from django.views.generic import CreateView

from .models import TargetUrl


def target_url_list(request):
    """Функция для отображения урлов"""
    urls = TargetUrl.objects.all()
    return render(request, 'webparser/list_url.html', context={'urls': urls})
