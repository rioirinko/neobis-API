from rest_framework import generics
from .serializers import *
from .models import *


class CoursesViewSet(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def perform_create(self, serializer):
        serializer.save()


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
