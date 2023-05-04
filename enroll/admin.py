from django.contrib import admin
from enroll.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password',)

'''
# Represents table data in admin site using ModelAdmin class
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password',)
admin.site.register(Student, StudentAdmin)'''

'''
# Raises error because of missing comma in ('id')
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id')
admin.site.register(Student, StudentAdmin)'''

'''
# Raises error is solved because of using comma in ('id',)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Student, StudentAdmin)
'''