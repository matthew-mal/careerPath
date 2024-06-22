from rest_framework.test import APITestCase
from rest_framework import status
from user.models import Employer, JobSeeker, User
from user.serializers import ProfileEmployerSerializer, ProfileJobSeekerSerializer


class EmployerViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(phone_number='11111111', email='testemail@test.com', username='testuser',
                                             password='password')
        self.employer = Employer.objects.create(company_name='Test Company')
        self.client.force_authenticate(user=self.employer)

    def test_get_profile(self):
        url = '/api/1/users/employers/profile/'
        response = self.client.get(url)

        serializer = ProfileEmployerSerializer(instance=self.employer)
        self.assertEqual(response.data, serializer.data)

    def test_update_profile(self):
        url = '/api/1/users/employers/profile/'
        new_company_name = 'Updated Company Name'
        data = {'company_name': new_company_name}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employer.refresh_from_db()
        self.assertEqual(self.employer.company_name, new_company_name)

    def test_update_profile_invalid_data(self):
        url = '/api/1/users/employers/profile/'
        data = {'industry': 'Invalid data'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_not_found(self):
        self.client.logout()
        url = '/api/1/users/employers/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class JobSeekerViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(phone_number='222222222', email='useremail@email.com', username='testuser',
                                             password='password')
        self.job_seeker = JobSeeker.objects.create(speciality='System Administrator')
        self.client.force_authenticate(user=self.job_seeker)

    def test_get_profile(self):
        url = '/api/1/users/job_seekers/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProfileJobSeekerSerializer(instance=self.job_seeker)
        self.assertEqual(response.data, serializer.data)

    def test_update_profile(self):
        url = '/api/1/users/job_seekers/profile/'
        new_speciality = 'Python Developer'
        data = {'new_speciality': new_speciality}

        # Make the PATCH request
        response = self.client.patch(url, data, format='json')

        # Check if the update was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh job_seeker instance from the database
        self.job_seeker.refresh_from_db()

        # Assert that the specialty has been updated correctly
        self.assertEqual(self.job_seeker.speciality, new_speciality)

    def test_update_profile_invalid_data(self):
        url = '/api/1/users/job_seekers/profile/'
        data = {'speciality': 'Invalid data'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_not_found(self):
        self.client.logout()
        url = '/api/1/users/job_seekers/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
