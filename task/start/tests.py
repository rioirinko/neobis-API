from django.test import TestCase
from start.models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.response import Response


class CourseTestCase(TestCase):
    def setUp(self):

        self.course_name = 'Dance'
        self.course_description = 'Dance go!'
        self.course_logo = 'Sun'
        self.course = Course(name=self.course_name, description=self.course_description, logo=self.course_logo,)

        self.category_name = 'Dance course'
        self.category = Category(name=self.category_name,)

        self.contact_type = 1
        self.contact_value = '0556123654'
        self.contact = Contact(type=self.contact_type, value=self.contact_value,)

        self.branch_address = 'Bishkek'
        self.branch_latitude = '2222'
        self.branch_longitude = '2223333'
        self.branch = Branch(address=self.branch_address, latitude=self.branch_latitude,
                             longitude=self.branch_longitude,)

    def test_model_can_create_a_course(self):
        old_count = Course.objects.count()
        self.course.save()
        new_count = Course.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_category(self):
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        self.assertEqual(str(self.course), self.course_name)
        self.assertEqual(str(self.category), self.category_name)


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course_data = {'name': 'Dance',
                            'description': 'Dance go!',
                            'logo': 'Sun',
                            'category': '',
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

        self.category_data = {
                                "name": "Dance course",
                                "imgpath": "/img.jpg",
                            }

        self.response = self.client.post(
            reverse('create'),
            self.course_data,
            format="json")

        self.response = self.client.post(
            reverse('category'),
            self.category_data,
            format="json")

    def test_api_can_create_a_course(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_create_category(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_course(self):
        try:
            courses = Course.objects.get(id=1)
            response = self.client.get(
                '/courses/',
                kwargs={'pk': courses.id}, format="json")
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, courses)

    def test_api_get_category(self):
        try:
            category = Category.objects.get(id=1)
            response = self.client.get(
                '/category/',
                kwargs={'pk': category.id})
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, category)