from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('reg1',views.TruckOwnerModel_View,basename='reg1')
# router.register('reg2',views.TruckOwnerVehicleRegistraionModel_View,basename='reg2')
# router.register('reg3',views.TruckOwnerDriverRegistration_View,basename='reg3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),
    # path('getuser/',views.student_data,name='stu'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

