from rest_framework import viewsets
from .serializers import VacancyListSerializer, VacancyCreateSerializer, ResponseSerializer, ChosenSerializer
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Vacancy, Chosen, Response
from user.models import UserType

from .paginations import VacancyPagination

from .filters import VacancyFilter


class VacancyViewSet(viewsets.ModelViewSet):
    """
    API viewset to handle listing, retrieving, creating, updating,
    and deleting vacancies with filtering, search, and ordering capabilities.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    pagination_class = VacancyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = VacancyFilter
    search_fields = ['category__title', 'speciality__title', 'industry__title']
    ordering_fields = ['salary', 'published_date']

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        if self.action == 'create':
            return VacancyCreateSerializer
        return VacancyListSerializer

    def perform_create(self, serializer):
        """
        Save the new vacancy if the requesting user is an authenticated employer.
        """
        user = self.request.user
        if user.is_authenticated and user.user_type == UserType.EMPLOYER:
            serializer.save(employer=user)
        else:
            raise PermissionDenied("Only employers can create vacancies")


class ResponseViewSet(viewsets.ModelViewSet):
    """
    API viewset to handle listing, retrieving, creating, updating,
    and deleting responses to vacancies.
    """
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def perform_create(self, serializer):
        """
        Save the response if the requesting user is an authenticated job seeker.
        """
        user = self.request.user
        if user.is_authenticated and user.user_type == UserType.JOB_SEEKER:
            serializer.save(user=user)
        else:
            raise PermissionDenied("Only job seekers can respond to vacancies")


class ChosenViewSet(viewsets.ModelViewSet):
    """
    API viewset to handle listing, retrieving, creating, updating,
    and deleting chosen vacancies by users.
    """
    serializer_class = ChosenSerializer

    def get_queryset(self):
        """
        Return the chosen vacancies for the requesting user.
        """
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this content")
        return Chosen.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Save the chosen vacancy for the requesting user.
        """
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            raise PermissionDenied("You must be logged in to create a chosen item")
