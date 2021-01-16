from django.urls import path, include
from rest_framework import routers
from .views import OperatingSystemViewSet

router = routers.DefaultRouter()
router.register(r'', OperatingSystemViewSet)

urlpatterns = [
	path('', include(router.urls))
]
