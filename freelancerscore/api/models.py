from django.db import models
from django.contrib.auth import get_user_model


class Skill(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name


class Experience(models.Model):
    company_name = models.CharField(max_length=60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    skills = models.ManyToManyField(Skill)


class Freelancer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    retribution = models.IntegerField()
    availability_date = models.DateTimeField()
    experiences = models.ManyToManyField(Experience)
