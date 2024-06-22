from rest_framework import generics, filters
from .models import Vacancy, Chosen
from user.models import UserType
from .serializers import (
    VacancyListSerializer,
    ResponseSerializer, VacancyCreateSerializer,
    ChosenSerializer
)

from rest_framework.exceptions import PermissionDenied
from .paginations import VacancyPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import VacancyFilter


class VacancyListView(generics.ListAPIView):
    """
    API view to retrieve a paginated list of vacancies with filtering,
    search, and ordering capabilities.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    pagination_class = VacancyPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = VacancyFilter
    search_fields = ['category__title']
    ordering_fields = ['salary']


class VacancyCreateView(generics.CreateAPIView):
    """
    API view to allow employers to create a new vacancy. Only users with
    an employer user type can create a vacancy.
    """
    serializer_class = VacancyCreateSerializer

    def perform_create(self, serializer):
        """
        Save the new vacancy if the requesting user is an authenticated employer.
        """
        user = self.request.user
        if user.is_authenticated and user.user_type == UserType.EMPLOYER:
            serializer.save(employer=user)
        else:
            raise PermissionDenied("Only employers can create vacancies")


class ResponseCreateView(generics.CreateAPIView):
    """
    API view to allow job seekers to respond to a vacancy. Only users with
    a job seeker user type can create a response.
    """
    serializer_class = ResponseSerializer

    def perform_create(self, serializer):
        """
        Save the new response if the requesting user is an authenticated job seeker.
        """
        user = self.request.user
        if user.is_authenticated and user.user_type == UserType.JOB_SEEKER:
            serializer.save(user=user)
        else:
            raise PermissionDenied("Only job seekers can respond to vacancies")


class ChosenListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of chosen vacancies for the authenticated user
    and allow them to add a new vacancy to their chosen list.
    """
    serializer_class = ChosenSerializer

    def get_queryset(self):
        """
        Retrieve the queryset of chosen vacancies for the authenticated user.
        """
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this content")
        return Chosen.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Save a new chosen vacancy for the authenticated user.
        """
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            raise PermissionDenied("You must be logged in to create a chosen item")
