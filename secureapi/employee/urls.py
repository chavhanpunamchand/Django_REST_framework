from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import EmpOperations
srouter = SimpleRouter()
srouter.register('emp',EmpOperations)
urlpatterns = srouter.urls
