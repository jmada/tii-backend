from django.urls import path, include
from rest_framework import routers
from .views import BrandViewSet

router = routers.DefaultRouter()
router.register(r'', BrandViewSet)

urlpatterns = [
	path('', include(router.urls))
]
