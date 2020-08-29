from medicines.models import medicine 
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import MedicineSerializer, MedicineListSerializer
from . import models
from knox.auth import TokenAuthentication

# Medicine Viewset
class MedicineViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MedicineSerializer
    
    # queryset = medicine.objects.all()
    def get_queryset(self):
        return self.request.user.medicines.all()

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)

class MedicineCountViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MedicineSerializer
    def list(self, request):
        queryset = medicine.objects.all()
        return Response(queryset.count())

class MedicineListSerializer(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MedicineListSerializer
    
    def get_queryset(self):
        return models.medicineslist.objects.all()

    def perform_create(self, serializer):
        serializer.save()