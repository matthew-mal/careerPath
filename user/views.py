from rest_framework import viewsets, status
from .models import Employer, JobSeeker
from .serializers import (
    EmployerListCreateSerializer, JobSeekerListCreateSerializer,
    ProfileEmployerSerializer, ProfileJobSeekerSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class EmployerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing employer instances.
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerListCreateSerializer

    @action(detail=False, methods=['get', 'patch'], url_path='profile', url_name='profile')
    def profile(self, request):
        """
        Retrieve or update the authenticated employer's profile.
        """
        user = get_object_or_404(Employer, id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileEmployerSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = ProfileEmployerSerializer(instance=user, data=request.data, partial=True,
                                                   context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobSeekerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing job seeker instances.
    """
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListCreateSerializer

    @action(detail=False, methods=['get', 'patch'], url_path='profile', url_name='profile')
    def profile(self, request):
        """
        Retrieve or update the authenticated job seeker's profile.
        """
        user = get_object_or_404(JobSeeker, id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileJobSeekerSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = ProfileJobSeekerSerializer(instance=user, data=request.data, partial=True,
                                                    context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
