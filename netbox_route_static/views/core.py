from dcim.models import Device
from netbox.views import generic
from utilities.views import register_model_view, ViewTab

from netbox_route_static.filtersets import StaticRouteFilterSet
from netbox_route_static.models import StaticRoute
from netbox_route_static.tables.static import StaticRouteTable


@register_model_view(Device, name='staticroutes', path='static_routes')
class DeviceStaticRoutesView(generic.ObjectChildrenView):
    template_name = 'generic/object_children.html'
    queryset = Device.objects.all()
    child_model = StaticRoute
    table = StaticRouteTable
    filterset = StaticRouteFilterSet
    tab = ViewTab(
        label='Static Routes',
        badge=lambda obj: StaticRoute.objects.filter(devices=obj).count(),
        permission='netbox_route_static.view_staticroute'
    )

    def get_children(self, request, device):
        return self.child_model.objects.filter(devices=device)
