from rest_framework import generics
from freelancerscore.api.serializers import FreelancerSerializer
from freelancerscore.api.models import Freelancer


class ListFreelancer(generics.ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
