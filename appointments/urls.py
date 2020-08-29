from rest_framework import routers
from .api import AppointmentViewSet, AppointmentCountViewSet


router = routers.DefaultRouter()
router.register('api/appointments', AppointmentViewSet,'appointments')
router.register('api/appointmentscount', AppointmentCountViewSet,'appointmentscount')

urlpatterns = router.urls