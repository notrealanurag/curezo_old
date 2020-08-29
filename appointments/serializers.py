from rest_framework import serializers
from appointments.models import appointment

class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = appointment 
    fields = '__all__'
