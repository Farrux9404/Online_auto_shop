from modeltranslation.translator import TranslationOptions, register
from .models import Logo, Car


@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)