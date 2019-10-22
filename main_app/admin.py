from django.contrib import admin

# Register your models here.

from .models import Plant
admin.site.register(Plant)
from .models import Dataplant
admin.site.register(Dataplant)