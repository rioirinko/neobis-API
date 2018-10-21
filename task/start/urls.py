from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^courses/$', views.CoursesDetailView.as_view(), name="create"),
}
urlpatterns = format_suffix_patterns(urlpatterns)