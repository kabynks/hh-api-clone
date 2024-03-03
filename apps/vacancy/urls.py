from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet

router = DefaultRouter()
router.register('vacancy', VacancyViewSet, basename='vacancy')

urlpatterns = [

]
urlpatterns += router.urls