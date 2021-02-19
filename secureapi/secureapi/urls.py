
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views
schema_view = get_swagger_view(title='API Security..!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include('address.urls')),
    path('v2/', include('employee.urls')),
    path('swagger/', schema_view),    # swagger  http://localhost:8000/
    path('api/', include('rest_framework.urls')), # rest api
    path('token/',views.obtain_auth_token)
]
