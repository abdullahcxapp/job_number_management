from rest_framework import viewsets
from .models import JobNumber
from jobs.serializer import JobNumberSerializer


class JobNumberViewSet(viewsets.ModelViewSet):

    queryset = JobNumber.objects.all()
    serializer_class = JobNumberSerializer
