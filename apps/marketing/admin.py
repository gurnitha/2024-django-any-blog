# apps/marketing/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.marketing.models import Signup

# Register your models here.
admin.site.register(Signup)
