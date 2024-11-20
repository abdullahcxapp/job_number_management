from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.views import JobNumberViewSet


router = DefaultRouter()
router.register(r'jobs', JobNumberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
