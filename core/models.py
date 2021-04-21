from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

@register_setting
class Setting(BaseSetting):
    
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = (
        ImageChooserPanel('favicon'),
        ImageChooserPanel('logo'),
    )
    
    class Meta:
        verbose_name = 'Configuraciones'
        verbose_name_plural = 'Configuraciones'