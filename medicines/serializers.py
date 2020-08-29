from rest_framework import serializers
from medicines.models import medicine , medicineslist

class MedicineSerializer(serializers.ModelSerializer):
  class Meta:
    model = medicine 
    fields = '__all__'

class MedicineListSerializer(serializers.ModelSerializer):
  class Meta:
    model = medicineslist
    fields = '__all__'