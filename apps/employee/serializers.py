from rest_framework.serializers import ModelSerializer
from .models import Employee, EmployeeSkill

class EmployeeSkillSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSkill
        fields = "__all__"

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
