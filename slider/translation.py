from slider.models import Slider
from modeltranslation.translator import register, TranslationOptions


@register(Slider)
class ScientistsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
