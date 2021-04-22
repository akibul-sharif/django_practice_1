from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'age',
        'address',
        'images'
    ]

admin.site.register(Profile,ProfileAdmin)

