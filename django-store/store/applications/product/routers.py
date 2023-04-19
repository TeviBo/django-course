# Django Rest Framework
from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r"api/colors", viewsets.ColorViewSet, basename="colors")
router.register(r"api/products", viewsets.ProductViewSet, basename="products")

urlpatterns = router.urls
