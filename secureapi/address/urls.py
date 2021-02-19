from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import *
srouter = SimpleRouter()
srouter.register('address',AddressOperations)
srouter.register('student',StudentOperations)
srouter.register('courses',CoursesOperations)

urlpatterns = srouter.urls
