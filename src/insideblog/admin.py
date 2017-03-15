from django.contrib import admin
from .models import article

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    pass
    #admin.site.register(article,articleAdmin)