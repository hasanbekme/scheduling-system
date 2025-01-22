from django.contrib import admin
from .models import Subject, Student, Tutor, Availability

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Availability)