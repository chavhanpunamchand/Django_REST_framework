from rest_framework.routers import SimpleRouter
from .views import EmpCrudAPIs
simple = SimpleRouter()
simple.register('api/v1',EmpCrudAPIs)

urlpatterns = simple.urls       # 6 urls-->
                            # create update:2 get:2 delete


#eMP OBJECT --> 10 FIELDS -->
                # METHOD1--> 2 FIELDS  --> SALARY ROLE --> PARTIAL UPDATE -- PATCH
                #METHOD2 --> ALL FIELDS --> ALL FIELDS --. FULL UPDATE --> PUT
