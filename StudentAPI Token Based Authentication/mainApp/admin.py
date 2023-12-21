from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','father_name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','category','book_title')

admin.site.register(Student,StudentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)

