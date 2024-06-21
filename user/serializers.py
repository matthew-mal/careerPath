from .models import Employer, JobSeeker
from rest_framework import serializers


class EmployerListCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and listing Employer instances.
    """

    class Meta:
        model = Employer
        fields = ['company_name', 'industry', 'other_industry', 'country', 'city', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Create a new Employer instance with a hashed password.

        Args:
            validated_data (dict): Validated data containing employer details and password.

        Returns:
            Employer: A newly created Employer instance.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Update an existing Employer instance and hash the password if provided.

        Args:
            instance (Employer): The Employer instance to update.
            validated_data (dict): Validated data containing updated employer details.

        Returns:
            Employer: The updated Employer instance.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class JobSeekerListCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and listing JobSeeker instances.
    """

    class Meta:
        model = JobSeeker
        fields = ['speciality', 'other_speciality', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Create a new JobSeeker instance with a hashed password.

        Args:
            validated_data (dict): Validated data containing job seeker details and password.

        Returns:
            JobSeeker: A newly created JobSeeker instance.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Update an existing JobSeeker instance and hash the password if provided.

        Args:
            instance (JobSeeker): The JobSeeker instance to update.
            validated_data (dict): Validated data containing updated job seeker details.

        Returns:
            JobSeeker: The updated JobSeeker instance.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileEmployerSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving and updating Employer profile details.
    """

    class Meta:
        model = Employer
        fields = ['company_name', 'industry', 'other_industry', 'country', 'city']


class ProfileJobSeekerSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving and updating JobSeeker profile details.
    """

    class Meta:
        model = JobSeeker
        fields = ['speciality', 'other_speciality']
