from rest_framework.serializers import ModelSerializer
from .models import Emp


# ModelSerializer --> based on model --> models fields la json madhe
# serialization
# model to json --->

class EmpToJson(ModelSerializer):
    class Meta:
        model = Emp  # fields to json
        fields = '__all__'
