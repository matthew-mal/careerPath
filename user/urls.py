from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet, JobSeekerViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'users'

router = DefaultRouter()
router.register(r'employers', EmployerViewSet, basename='employers')
router.register(r'job_seekers', JobSeekerViewSet, basename='job_seekers')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
