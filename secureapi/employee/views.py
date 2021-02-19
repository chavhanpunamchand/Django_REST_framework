from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import Emp
from .serializers import EmpSerialization
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BaseAuthentication
#rest_framework.authentication.TokenAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

#object level permission
class MyCustomPersmission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) and self.has_object_permission(request,view,None)

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            data = request.data
            if data.get('age')>30:
                return True
            return False
        return True


class EmpOperations(ModelViewSet):
    permission_classes = (MyCustomPersmission,)
    queryset = Emp.objects.all()
    serializer_class = EmpSerialization
    #`create()`, `retrieve()`, `update()`,
    #`partial_update()`, `destroy()` and `list()
    '''
    def get_permissions(self):
        if self.action in ['create','destroy']:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()
    '''



