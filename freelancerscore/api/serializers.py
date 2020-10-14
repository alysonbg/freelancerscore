from rest_framework import serializers
from freelancerscore.api.models import Experience, Freelancer, Skill
from django.contrib.auth import get_user_model


user_model = get_user_model()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerialzer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    companyName = serializers.CharField(source='company_name')
    startDate = serializers.DateTimeField(source='start_date')
    endDate = serializers.DateTimeField(source='end_date')

    class Meta:
        model = Experience
        fields = ['id', 'companyName', 'startDate', 'endDate', 'skills']


class FreelancerSerializer(serializers.ModelSerializer):
    professionalExperiences = ExperienceSerialzer(many=True, source='experiences')
    availabilityDate = serializers.DateTimeField(source='availability_date')

    class Meta:
        model = Freelancer
        fields = ['id', 'status', 'retribution', 'professionalExperiences', 'availabilityDate']

    def create(self, validated_data):
        experiences = validated_data.pop('experiences')
        freelancer = Freelancer.objects.create(**validated_data)
        for experience in experiences:
            skills = experience.pop('skills')
            exp = Experience.objects.create(**experience)
            for skill in skills:
                skill_instance = Skill.objects.get_or_create(name=skill.get('name'))
                exp.skills.add(skill_instance[0])
            freelancer.experiences.add(exp)

        return freelancer
