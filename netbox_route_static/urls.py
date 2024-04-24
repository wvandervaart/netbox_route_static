from django.urls import path

from netbox.views.generic import ObjectChangeLogView

from . import views
from .models import StaticRoute

urlpatterns = [
    path('routes/static/', views.StaticRouteListView.as_view(), name='staticroute_list'),
    path('routes/static/add/', views.StaticRouteEditView.as_view(), name='staticroute_add'),
    path('routes/static/import/', views.StaticRouteListView.as_view(), name='staticroute_import'),
    path('routes/static/<int:pk>/', views.StaticRouteView.as_view(), name='staticroute'),
    path('routes/static/<int:pk>/edit/', views.StaticRouteEditView.as_view(), name='staticroute_edit'),
    path('routes/static/<int:pk>/devices/', views.StaticRouteDevicesView.as_view(), name='staticroute_devices'),
    path('routes/static/<int:pk>/delete/', views.StaticRouteDeleteView.as_view(), name='staticroute_delete'),
    path('routes/static/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='staticroute_changelog', kwargs={'model': StaticRoute}),
]
