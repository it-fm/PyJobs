from pyjobs.core.models import Job, STATE_CHOICES, SALARY_RANGES, JOB_LEVELS
import django_filters


class JobFilter(django_filters.FilterSet):
    state = django_filters.ChoiceFilter(choices=STATE_CHOICES[:-1])
    salary_range = django_filters.ChoiceFilter(choices=SALARY_RANGES[:-1])
    job_level = django_filters.ChoiceFilter(choices=JOB_LEVELS[:-1])

    class Meta:
        model = Job
        fields = ["title", "state", "salary_range", "job_level", "remote", "skills"]
