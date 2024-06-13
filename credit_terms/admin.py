from django.contrib import admin
from .models import Credit_terms

@admin.register(Credit_terms)
class CredittermsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'file',)


