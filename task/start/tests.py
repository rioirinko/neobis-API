from django.test import TestCase
from start.models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class CoursesTestCase(TestCase):
    def setUp(self):

        self.courses_name = 'Dance'
        self.courses_description = 'Dad'
        self.courses_category = 'Cat'
        self.courses_logo = 'Sun'
        self.courses = Courses(name=self.courses_name, description=self.courses_description,
                               category=self.courses_category, logo=self.courses_logo,)

        self.contact_type = 1
        self.contact_value = '0556123654'
        self.contact = Contact(type=self.contact_type, value=self.contact_value,)

        self.branch_address = 'Bishkek'
        self.branch_latitude = '2222'
        self.branch_longitude = '2223333'
        self.branch = Branch(address=self.branch_address, latitude=self.branch_latitude,
                             longitude=self.branch_longitude,)

    def test_model_can_create_a_courses(self):
        old_count = Courses.objects.count()
        self.courses.save()
        new_count = Courses.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        self.assertEqual(str(self.courses), self.courses_name)


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.courses_data = {'name': 'Dance',
                             'description': 'Dad',
                             'category': 'Cat',
                             'logo': 'Sun',
                             'contacts': [
                                 {
                                     'type': '1',
                                     'value': '0556123654',
                                 }
                             ],
                             'branches': [
                                 {
                                     'address': 'Bishkek',
                                     'latitude': '2222',
                                     'longitude': '2223333',
                                 }
                             ],
                             }
        self.response = self.client.post(
            reverse('create'),
            self.courses_data,
            format="json")

    def test_api_can_create_a_courses(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_courses(self):
        courses = Courses.objects.get(id=1)
        response = self.client.get(
            '/courses/',
            kwargs={'pk': courses.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, courses)