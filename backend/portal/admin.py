from django.contrib import admin

# Register your models here.
from .models import Telecommunications, GovernmentID


admin.site.register(Telecommunications)
admin.site.register(GovernmentID)
