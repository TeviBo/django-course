# Django Rest Framewor
from rest_framework.routers import DefaultRouter

# Viewsets
from . import viewsets

router = DefaultRouter()
router.register(r"api/sales", viewsets.SalesViewSet, basename="sales")

urlpatterns = router.urls
