from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Todoviewset

router = DefaultRouter()
router.register(r'todos', Todoviewset)

urlpatterns = [
    path('',include(router.urls))
]
