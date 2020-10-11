from django.urls import path
from freelancerscore.api.views import ListFreelancer


urlpatterns = [
    path('freelancers/', ListFreelancer.as_view(), name='list-freelancers'),
]
