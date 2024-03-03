from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, EmployeeSkillViewSet
from django.urls import path,include

router = DefaultRouter()
router.register("employee-skills", EmployeeSkillViewSet, basename="employee-skills")
router.register("employee", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("", include(router.urls))
]