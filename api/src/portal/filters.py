import django_filters
from django_filters import DateFilter, CharFilter

from api.src.tickets.models.models import Bus, Route, Schedule


class ScheduleFilter(django_filters.rest_framework.FilterSet):
	class Meta:
		model = Schedule
		fields = ['route__from_destination','route__to_destination','date_of_travel']
