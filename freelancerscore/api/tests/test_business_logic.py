from freelancerscore.api import business_logic
import pytest
from freelancerscore.api.models import Experience, Freelancer, Skill
from model_bakery import baker
from dateutil.parser import parse


@pytest.fixture
def skills(db):
    return [baker.make(Skill) for i in range(5)]


@pytest.fixture
def experiences(db, skills):
    experience1 = baker.make(Experience, start_date=parse('2013-05-01T00:00:00+01:00'),
                             end_date=parse('2013-12-01T00:00:00+01:00'))
    experience2 = baker.make(Experience, start_date=parse('2014-01-01T00:00:00+01:00'),
                             end_date=parse('2015-02-01T00:00:00+01:00'))
    for skill in skills:
        experience1.skills.add(skill)
        experience2.skills.add(skill)

    return [experience1, experience2]


@pytest.fixture
def freelancer(db, experiences):
    freelancer = baker.make(Freelancer)
    for experience in experiences:
        freelancer.experiences.add(experience)
    return freelancer


def test_compute_score_from_experience(db, experiences):
    experience = experiences[0]
    skills_list = [skill for skill in experience.skills.all()]
    experience_data = {'skills': skills_list, 'durationInMonths': 7}

    assert business_logic._compute_score_from_experience(experience) == experience_data


def test_compute_score(db, freelancer, skills):
    score = business_logic.compute_score(freelancer)
    skills_data = [{'id': skill.id, 'name': skill.name, 'durationInMonths': 20} for skill in skills]

    assert score == skills_data
