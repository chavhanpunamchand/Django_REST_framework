from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Employee Emps')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',include('rest_demo.urls')), # viewset-- our
    url(r'^$', schema_view),    # swagger
    path('api-auth/', include('rest_framework.urls')) # rest api

]
