from rest_framework import routers

from django.urls import path, include

from judge.views import UploadViewSet

router = routers.SimpleRouter()
router.register(r'submit', UploadViewSet, basename="upload")

urlpatterns = [path('', include(router.urls))]
