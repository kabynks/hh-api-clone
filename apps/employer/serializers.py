from .models import Employer
from rest_framework.serializers import ModelSerializer

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"