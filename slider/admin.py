from django.contrib import admin

from slider.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'image',)


