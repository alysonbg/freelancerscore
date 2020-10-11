from rest_framework import serializers
from freelancerscore.api.models import Experience, Freelancer, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerialzer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Experience
        fields = ['id', 'company_name', 'start_date', 'end_date', 'skills']


class FreelancerSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerialzer(many=True)

    class Meta:
        model = Freelancer
        fields = ['id', 'user', 'status', 'retribution', 'experiences']
