from django.test import TestCase
from user.forms import EmployerCreationForm, EmployerChangeForm, JobSeekerCreationForm, JobSeekerChangeForm
from user.models import Employer, JobSeeker


class EmployerCreationFormTest(TestCase):
    def test_employer_creation_form_valid(self):
        form_data = {
            'phone_number': '1234567890',
            'username': 'employeruser',
            'email': 'employer@example.com',
            'is_active': True,
            'password1': 'password123',
            'password2': 'password123',
        }
        form = EmployerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_employer_creation_form_blank_username(self):
        form_data = {
            'phone_number': '1234567890',
            'username': '',  # blank username
            'email': 'employer@example.com',
            'is_active': True,
            'password1': 'password123',
            'password2': 'password123',
        }
        form = EmployerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_employer_creation_form_existing_email(self):
        existing_user = Employer.objects.create_user(phone_number='1234567890',username='existinguser', email='employer1@example.com')
        form_data = {
            'phone_number': '1234567890', # phone_number already exists
            'username': 'employeruser',
            'email': 'employer@example.com',
            'is_active': True,
            'password1': 'password123',
            'password2': 'password123',
        }
        form = EmployerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)


class EmployerChangeFormTest(TestCase):
    def test_employer_change_form_valid(self):
        employer = Employer.objects.create_user(phone_number='111', username='employeruser', email='employer@example.com')
        form_data = {
            'password': employer.password,
            'is_admin': False,
            'is_active': True,
        }
        form = EmployerChangeForm(instance=employer, data=form_data)
        self.assertTrue(form.is_valid())


class JobSeekerCreationFormTest(TestCase):
    def test_jobseeker_creation_form_valid(self):
        form_data = {
            'phone_number': '1234567890',
            'username': 'jobseekeruser',
            'email': 'jobseeker@example.com',
            'is_active': True,
            'password1': 'password123',
            'password2': 'password123',
        }
        form = JobSeekerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_jobseeker_creation_form_blank_email(self):
        form_data = {
            'phone_number': '1234567890',
            'username': 'jobseekeruser',
            'email': '',  # blank email
            'is_active': True,
            'password1': 'password123',
            'password2': 'password123',
        }
        form = JobSeekerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class JobSeekerChangeFormTest(TestCase):
    def test_jobseeker_change_form_valid(self):
        jobseeker = JobSeeker.objects.create_user(phone_number='111',username='jobseekeruser', email='jobseeker@example.com')
        form_data = {
            'password': jobseeker.password,
            'is_admin': False,
            'is_active': True,
        }
        form = JobSeekerChangeForm(instance=jobseeker, data=form_data)
        self.assertTrue(form.is_valid())
