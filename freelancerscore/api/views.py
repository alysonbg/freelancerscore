from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from freelancerscore.api.serializers import FreelancerSerializer
from freelancerscore.api.models import Freelancer
from freelancerscore.api import business_logic
from rest_framework import status


class ListFreelancer(generics.ListCreateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer


class FreelancerScore(APIView):
    def get(self, request, *args, **kwargs):
        freelancer = Freelancer.objects.get(pk=kwargs.get('pk'))
        freelancer_computed_skills = business_logic.compute_score(freelancer)
        data = {
            'freelancer': {
                'id': freelancer.id,
                'computedSkills': freelancer_computed_skills
            }
        }

        return Response(data, status=status.HTTP_200_OK)
