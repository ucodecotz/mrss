from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


# Register your models here.
class ProblemsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ("title",)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Solution)
admin.site.register(Comments)
# admin.site.register(BlogPost)
admin.site.register(UserProfile)
admin .site.unregister(Group)


