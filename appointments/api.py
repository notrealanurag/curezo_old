from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import AppointmentSerializer
from . import models
from knox.auth import TokenAuthentication

# Medicine Viewset
class AppointmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AppointmentSerializer
    
    # queryset = medicine.objects.all()
    def get_queryset(self):
        return self.request.user.appointments.all()

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)

class AppointmentCountViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AppointmentSerializer
    def list(self, request):
        queryset = appointment.objects.all()
        return Response(queryset.count())
