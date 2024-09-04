from django.contrib import admin
from .models import Job , Category , Apply

# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)


admin.site.site_header='Job Board'
admin.site.site_title='Job Board'