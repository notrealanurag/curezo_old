from rest_framework import routers
from .api import MedicineViewSet, MedicineCountViewSet, MedicineListSerializer


router = routers.DefaultRouter()
router.register('api/medicines', MedicineViewSet,'medicines')
router.register('api/medicinescount', MedicineCountViewSet,'medicinescount')
router.register('api/medicineslist', MedicineListSerializer,'medicineslist')

urlpatterns = router.urls