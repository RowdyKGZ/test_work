from django.urls import path

from .views import target_url_list

urlpatterns = [
    path('', target_url_list, name='create_target_url'),
]
