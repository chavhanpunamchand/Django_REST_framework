from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from testapp import views

router=routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)
from rest_framework.authtoken import views

schema_view = get_swagger_view(title='Employee Emps')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('emp/',include('rest_demo.urls')), # viewset-- our
    # url(r'^$', schema_view),    # swagger
    url(r'^$',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')) # rest api
    path('^get-api-token/', views.obtain_auth_token,name='get-api-token')

]
