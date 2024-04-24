from netbox.api.routers import NetBoxRouter
from .views import StaticRouteViewSet

router = NetBoxRouter()
router.register('staticroute', StaticRouteViewSet)
urlpatterns = router.urls
