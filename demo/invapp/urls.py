from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TuoteViewSet, VarastotViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tuotteet', TuoteViewSet, basename='tuote')
router.register(r'varastot', views.VarastotViewSet, basename='varastot')

urlpatterns = [
    
    path('varasto/', views.varasto, name='varasto'),
    path('', include(router.urls)),
    path('users/', UserViewSet.as_view(), name='user-create'),
]