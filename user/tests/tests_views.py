from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import check_password
from user.models import Employer, JobSeeker  # Подставьте правильный импорт для моделей
from user.serializers import EmployerListCreateSerializer, JobSeekerListCreateSerializer
from rest_framework.reverse import reverse


class EmployerSerializerAPITestCase(APITestCase):
    def setUp(self):
        self.validated_data = {
            'company_name': 'Test Company',
            'industry': 'IT',
            'other_industry': 'Tech',
            'country': 'USA',
            'city': 'New York',
            'password': 'testpassword123'
        }

    def test_create_employer(self):
        url = reverse('users:employers-list')
        response = self.client.post(url, self.validated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        employer_instance = Employer.objects.get(id=response.data['id'])
        self.assertEqual(employer_instance.company_name, self.validated_data['company_name'])
        self.assertEqual(employer_instance.industry, self.validated_data['industry'])
        self.assertEqual(employer_instance.other_industry, self.validated_data['other_industry'])
        self.assertEqual(employer_instance.country, self.validated_data['country'])
        self.assertEqual(employer_instance.city, self.validated_data['city'])
        self.assertTrue(check_password(self.validated_data['password'], employer_instance.password))

    def test_update_employer(self):
        employer_instance = Employer.objects.create(**self.validated_data)
        new_data = {
            'company_name': 'Updated Company',
            'industry': 'Finance',
            'other_industry': 'Banking',
            'country': 'UK',
            'city': 'London',
            'password': 'updatedpassword456'
        }

        url = reverse('users:employers-detail',
                      args=[employer_instance.id])  # Получаем URL через reverse для конкретного работодателя
        response = self.client.put(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = Employer.objects.get(id=employer_instance.id)
        self.assertEqual(updated_instance.company_name, new_data['company_name'])
        self.assertEqual(updated_instance.industry, new_data['industry'])
        self.assertEqual(updated_instance.other_industry, new_data['other_industry'])
        self.assertEqual(updated_instance.country, new_data['country'])
        self.assertEqual(updated_instance.city, new_data['city'])
        self.assertTrue(check_password(new_data['password'], updated_instance.password))


class JobSeekerSerializerAPITestCase(APITestCase):
    def setUp(self):
        self.validated_data = {
            'speciality': 'Software Engineering',
            'other_speciality': 'DevOps',
            'password': 'seekerpassword789'
        }

    def test_create_jobseeker(self):
        url = reverse('users:jobseekers-list')  # Получаем URL через reverse для списка соискателей работы
        response = self.client.post(url, self.validated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        jobseeker_instance = JobSeeker.objects.get(id=response.data['id'])
        self.assertEqual(jobseeker_instance.speciality, self.validated_data['speciality'])
        self.assertEqual(jobseeker_instance.other_speciality, self.validated_data['other_speciality'])
        self.assertTrue(check_password(self.validated_data['password'], jobseeker_instance.password))

    def test_update_jobseeker(self):
        jobseeker_instance = JobSeeker.objects.create(**self.validated_data)
        new_data = {
            'speciality': 'Data Science',
            'other_speciality': 'Machine Learning',
            'password': 'updatedseeker123'
        }

        url = reverse('users:jobseekers-detail',
                      args=[jobseeker_instance.id])  # Получаем URL через reverse для конкретного соискателя работы
        response = self.client.put(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = JobSeeker.objects.get(id=jobseeker_instance.id)
        self.assertEqual(updated_instance.speciality, new_data['speciality'])
        self.assertEqual(updated_instance.other_speciality, new_data['other_speciality'])
        self.assertTrue(check_password(new_data['password'], updated_instance.password))
