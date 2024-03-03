from rest_framework.viewsets import ModelViewSet
from .serializers import EmployerSerializer
from .models import Employer

class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
