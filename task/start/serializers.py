from rest_framework import serializers
from .models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value',)


class CoursesSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Courses
        fields = ('id', 'name', 'logo', 'category', 'description', 'contacts', 'branches')

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        courses = Courses.objects.create(**validated_data)
        
        for contact in contacts:
            Contact.objects.create(courses=courses, **contact)
        for branch in branches:
            Branch.objects.create(courses=courses, **branch)

        return courses