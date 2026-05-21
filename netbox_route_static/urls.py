from django.urls import path, include

from netbox.views.generic import ObjectChangeLogView

from . import views
from .models import StaticRoute

urlpatterns = [
    path(
        'routes/static/', include(get_model_urls(app_name, 'staticroute', detail=False))
    ),
    path('routes/static/<int:pk>/', include(get_model_urls(app_name, 'staticroute'))),
]
