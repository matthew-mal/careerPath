from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet, ResponseViewSet, ChosenViewSet

app_name = 'jobs'

router = DefaultRouter()
router.register(r'vacancies', VacancyViewSet, basename='vacancy')
router.register(r'responses', ResponseViewSet, basename='response')
router.register(r'chosen', ChosenViewSet, basename='chosen')

urlpatterns = [
    path('', include(router.urls)),
]
