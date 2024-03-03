from rest_framework.viewsets import ModelViewSet
from .serializers import VacancySerializer
from .models import Vacancy

class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
