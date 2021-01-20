from django.urls import path

from .views import TargetUrlView

urlpatterns = [
    path('', TargetUrlView.as_view(), name='create_target_url'),
]
