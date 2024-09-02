from django.contrib import admin
from .models import Job , Category

# Register your models here.
admin.site.register(Job)
admin.site.register(Category)


admin.site.site_header='Job Board'
admin.site.site_title='Job Board'