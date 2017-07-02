from django.contrib import admin
from .models import TeacherProfile, StudentProfile, Attendence

admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(Attendence)
admin.site.site_header = 'Krishna College Administration'