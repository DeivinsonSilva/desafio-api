from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from sigma.views import QuotesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quotes', QuotesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
