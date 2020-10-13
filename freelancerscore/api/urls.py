from django.urls import path
from freelancerscore.api.views import FreelancerScore, ListFreelancer


urlpatterns = [
    path('freelancers/', ListFreelancer.as_view(), name='list-freelancers'),
    path('freelancers/<int:pk>/score/', FreelancerScore.as_view(), name='freelancer-score')
]
