from netbox.api.viewsets import NetBoxModelViewSet
from netbox_route_static import filtersets
from netbox_route_static.api.serializers import StaticRouteSerializer
from netbox_route_static.models import StaticRoute


class StaticRouteViewSet(NetBoxModelViewSet):
    queryset = StaticRoute.objects.all()
    serializer_class = StaticRouteSerializer
    filterset_class = filtersets.StaticRouteFilterSet
