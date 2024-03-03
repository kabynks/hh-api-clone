from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('employer', EmployerViewSet, basename='employer')

urlpatterns = [
    path("", include(router.urls))
]