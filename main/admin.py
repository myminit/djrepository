from django.contrib import admin

# Register your models here.
from .models import Company, PreviousJob

admin.site.register(Company)
admin.site.register(PreviousJob)