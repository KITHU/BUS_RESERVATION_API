from django.contrib import admin
from .models.models import Bus, Route, Schedule

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Schedule)
