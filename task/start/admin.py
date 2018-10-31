from django.contrib import admin
from .models import *


class BranchInline(admin.StackedInline):
    model = Branch
    extra = 0


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [ContactInline, BranchInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Category)