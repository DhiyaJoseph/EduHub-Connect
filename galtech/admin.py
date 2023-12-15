from django.contrib import admin
from . models import UsersProfile,courses,Lessons,Video,Reviews

# Register your models here.
admin.site.register(UsersProfile)
admin.site.register(courses)
admin.site.register(Lessons)
admin.site.register(Video)
admin.site.register(Reviews)