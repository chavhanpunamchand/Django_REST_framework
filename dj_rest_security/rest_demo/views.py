#ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from .models import Emp
from .empserializer import EmpToJson
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin

# class MyOwnViewSet(GenericViewSet,DestroyModelMixin,UpdateModelMixin):
#     pass


# model to json
class EmpCrudAPIs(ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpToJson