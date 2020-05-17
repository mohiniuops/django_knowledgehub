from django.contrib import admin
from .models import app_name,doccat,appcat

# Register your models here.

admin.site.register(app_name)
admin.site.register(doccat)
admin.site.register(appcat)