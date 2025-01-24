from rest_framework import serializers

from dcim.api.serializers import DeviceSerializer
from ipam.api.serializers import VRFSerializer
from netbox.api.serializers import NetBoxModelSerializer
from netbox_route_static.models import StaticRoute


__all__ = (
    'StaticRouteSerializer'
)


class StaticRouteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_route_static-api:staticroute-detail')
    devices = DeviceSerializer(many=True, nested=True)
    vrf = VRFSerializer(nested=True)

    class Meta:
        model = StaticRoute
        fields = ('url', 'id', 'display', 'devices', 'vrf', 'prefix', 'next_hop', 'name', 'metric', 'permanent', 'custom_fields')
