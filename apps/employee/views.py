from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer, EmployeeSkillSerializer
from .models import Employee, EmployeeSkill

class EmployeeSkillViewSet(ModelViewSet):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
