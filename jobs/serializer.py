from rest_framework import serializers
from .models import JobNumber


class JobNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobNumber
        fields = '__all__'
