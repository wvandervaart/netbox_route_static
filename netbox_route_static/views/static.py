from dcim.filtersets import DeviceFilterSet
from dcim.models import Device
from dcim.tables import DeviceTable
from netbox.views.generic import (
    ObjectListView,
    ObjectEditView,
    ObjectView,
    ObjectDeleteView,
    ObjectChildrenView,
    BulkDeleteView,
    BulkEditView,
    BulkImportView,
)
from netbox_route_static.filtersets.static import StaticRouteFilterSet
from netbox_route_static.forms import StaticRouteForm
from netbox_route_static.forms.bulk_edit import StaticRouteBulkEditForm
from netbox_route_static.forms.filtersets.static import StaticRouteFilterForm
from netbox_route_static.forms.bulk_import import StaticRouteImportForm
from netbox_route_static.models import StaticRoute
from netbox_route_static.tables.static import StaticRouteTable


__all__ = (
    'StaticRouteListView',
    'StaticRouteView',
    'StaticRouteDevicesView',
    'StaticRouteEditView',
    'StaticRouteBulkEditView',
    'StaticRouteDeleteView',
    'StaticRouteBulkDeleteView',
    'StaticRouteBulkImportView',
)

from utilities.views import register_model_view, ViewTab


@register_model_view(StaticRoute, name='list')
class StaticRouteListView(ObjectListView):
    queryset = StaticRoute.objects.all()
    table = StaticRouteTable
    filterset = StaticRouteFilterSet
    filterset_form = StaticRouteFilterForm


@register_model_view(StaticRoute)
class StaticRouteView(ObjectView):
    queryset = StaticRoute.objects.all()
    template_name = 'netbox_route_static/staticroute.html'

@register_model_view(StaticRoute, name='devices')
class StaticRouteDevicesView(ObjectChildrenView):
    template_name = 'netbox_route_static/staticroute_devices.html'
    queryset = StaticRoute.objects.all()
    child_model = Device
    table = DeviceTable
    filterset = DeviceFilterSet
    actions = []
    tab = ViewTab(
        label='Assigned Devices',
        badge=lambda obj: Device.objects.filter(static_routes=obj).count(),
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(static_routes=parent)


@register_model_view(StaticRoute, name='edit')
class StaticRouteEditView(ObjectEditView):
    queryset = StaticRoute.objects.all()
    form = StaticRouteForm


@register_model_view(StaticRoute, name='delete')
class StaticRouteDeleteView(ObjectDeleteView):
    queryset = StaticRoute.objects.all()
    pass

@register_model_view(StaticRoute, name='bulk_edit', detail=False)
class StaticRouteBulkEditView(BulkEditView):
    queryset = StaticRoute.objects.all()
    filterset = StaticRouteFilterSet
    table = StaticRouteTable
    form = StaticRouteBulkEditForm


@register_model_view(StaticRoute, name='bulk_delete', detail=False)
class StaticRouteBulkDeleteView(BulkDeleteView):
    queryset = StaticRoute.objects.all()
    filterset = StaticRouteFilterSet
    table = StaticRouteTable

@register_model_view(StaticRoute, name='bulk_import', detail=False)
class StaticRouteBulkImportView(BulkImportView):
    queryset = StaticRoute.objects.all()
    model_form = StaticRouteImportForm