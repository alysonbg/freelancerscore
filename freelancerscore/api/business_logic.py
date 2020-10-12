from freelancerscore.api.models import Experience, Freelancer
from dateutil.relativedelta import relativedelta


def compute_score(freelancer: Freelancer):
    """
    Compute the amount of months of experience for each experience
    """
    scores = {}

    for experience in freelancer.experiences.all():
        score_skill = _compute_score_from_experience(experience)

        for skill in score_skill['skills']:
            if skill.name not in scores.keys():
                scores[skill.name] = {
                    'id': skill.id,
                    'name': skill.name,
                    'durationInMonths': score_skill['durationInMonths']
                }
            else:
                scores[skill.name]['durationInMonths'] += score_skill['durationInMonths']

    return [
        {'id': scores[skill]['id'],
         'name': skill,
         'durationInMonths': scores[skill]['durationInMonths']} for skill in scores
    ]


def _compute_score_from_experience(experience: Experience):
    """
    Compute the amount of experience per skill
    """
    duration_in_months = relativedelta(experience.end_date, experience.start_date).years * 12 +\
        relativedelta(experience.end_date, experience.start_date).months
    skills = [skill for skill in experience.skills.all()]

    return {
        'skills': skills,
        'durationInMonths': duration_in_months
    }
