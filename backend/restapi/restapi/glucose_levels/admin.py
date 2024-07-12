from django.contrib import admin
from .models import User, GlucoseLevel

# Register your models here.
admin.site.register(User)
admin.site.register(GlucoseLevel)
