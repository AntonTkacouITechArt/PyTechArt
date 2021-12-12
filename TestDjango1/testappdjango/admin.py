from django.contrib import admin

# Register your models here.
from testappdjango.models import Student, Teacher, Mark

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Mark)





