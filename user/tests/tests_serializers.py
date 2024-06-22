from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import check_password
from user.models import Employer, JobSeeker
from rest_framework.reverse import reverse


class EmployerSerializerAPITestCase(APITestCase):
    def setUp(self):
        self.validated_data = {
            'company_name': 'Test Company',
            'industry': 'Web Development',
            'other_industry': 'Database Management',
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
            'industry': 'Cybersecurity',
            'other_industry': 'IT Consulting',
            'country': 'UK',
            'city': 'London',
            'password': 'updatedpassword456'
        }

        url = reverse('users:employers-detail', args=[employer_instance.id])
        response = self.client.put(url, new_data, format='json')

        # Выводим содержимое response.data в случае ошибки
        if response.status_code != status.HTTP_200_OK:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = Employer.objects.get(id=employer_instance.id)
        self.assertEqual(updated_instance.company_name, new_data['company_name'])
        self.assertEqual(updated_instance.industry, new_data['industry'])
        self.assertEqual(updated_instance.other_industry, new_data['other_industry'])
        self.assertEqual(updated_instance.country, new_data['country'])
        self.assertEqual(updated_instance.city, new_data['city'])
        self.assertTrue(check_password(new_data['password'], updated_instance.password))

    def test_retrieve_employer(self):
        employer_instance = Employer.objects.create(**self.validated_data)
        url = reverse('users:employers-detail', args=[employer_instance.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], self.validated_data['company_name'])
        self.assertEqual(response.data['industry'], self.validated_data['industry'])


class EmployerListAPITestCase(APITestCase):
    def setUp(self):
        self.employers_data = [
            {
                'company_name': 'Test Company 1',
                'industry': 'Web Development',
                'country': 'USA',
                'city': 'New York',
                'phone_number': '1111111111'
            },
            {
                'company_name': 'Test Company 2',
                'industry': 'Database Management',
                'country': 'UK',
                'city': 'London',
                'phone_number': '2222222222'
            },
            {
                'company_name': 'Test Company 3',
                'industry': 'Cybersecurity',
                'country': 'Canada',
                'city': 'Toronto',
                'phone_number': '3333333333'
            }
        ]
        for employer_data in self.employers_data:
            Employer.objects.create(**employer_data)

    def test_list_employers(self):
        url = reverse('users:employers-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.employers_data))

        for employer_data in response.data:
            employer_instance = Employer.objects.get(id=employer_data['id'])
            self.assertEqual(employer_data['company_name'], employer_instance.company_name)
            self.assertEqual(employer_data['industry'], employer_instance.industry)


class JobSeekerSerializerAPITestCase(APITestCase):
    def setUp(self):
        self.validated_data = {
            'speciality': 'Python Developer',
            'other_speciality': 'Data Scientist',
            'password': 'seekerpassword789',
            'phone_number': '1234567890'
        }
        self.jobseeker_instance = JobSeeker.objects.create(**self.validated_data)

    def test_create_jobseeker(self):
        url = reverse('users:job_seekers-list')
        response = self.client.post(url, self.validated_data, format='json')

        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        jobseeker_instance = JobSeeker.objects.get(id=response.data['id'])
        self.assertEqual(jobseeker_instance.speciality, self.validated_data['speciality'])
        self.assertEqual(jobseeker_instance.other_speciality, self.validated_data['other_speciality'])
        self.assertTrue(check_password(self.validated_data['password'], jobseeker_instance.password))

    def test_update_jobseeker(self):
        new_data = {
            'speciality': 'Data Scientist',
            'other_speciality': 'Android Developer',
            'password': 'updatedseeker123',
            'phone_number': '0987654321'
        }

        url = reverse('users:job_seekers-detail', args=[self.jobseeker_instance.id])
        response = self.client.put(url, new_data, format='json')

        if response.status_code != status.HTTP_200_OK:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = JobSeeker.objects.get(id=self.jobseeker_instance.id)
        self.assertEqual(updated_instance.speciality, new_data['speciality'])
        self.assertEqual(updated_instance.other_speciality, new_data['other_speciality'])
        self.assertTrue(check_password(new_data['password'], updated_instance.password))

    def test_list_jobseekers(self):
        url = reverse('users:job_seekers-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        jobseeker_data = response.data[0]
        self.assertEqual(jobseeker_data['speciality'], self.jobseeker_instance.speciality)
        self.assertEqual(jobseeker_data['other_speciality'], self.jobseeker_instance.other_speciality)

    def test_retrieve_jobseeker(self):
        url = reverse('users:job_seekers-detail', args=[self.jobseeker_instance.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['speciality'], self.jobseeker_instance.speciality)
        self.assertEqual(response.data['other_speciality'], self.jobseeker_instance.other_speciality)

    def test_delete_jobseeker(self):
        url = reverse('users:job_seekers-detail', args=[self.jobseeker_instance.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(JobSeeker.objects.filter(id=self.jobseeker_instance.id).exists())

    def test_create_jobseeker_invalid_password(self):
        invalid_data = {
            'speciality': 'Data Scientist',
            'other_speciality': 'Data Scientist',
            'password': ''
        }
        url = reverse('users:job_seekers-list')
        response = self.client.post(url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_create_jobseeker_invalid_data(self):
        invalid_data = {
            'speciality': 'Finance',
            'other_speciality': 'Law',
            'password': 'testpassword'
        }
        url = reverse('users:job_seekers-list')
        response = self.client.post(url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('speciality', response.data)

