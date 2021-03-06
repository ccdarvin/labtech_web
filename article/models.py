from django.db import models
from wagtail.core.models import Page
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtailmarkdown.blocks import MarkdownBlock
from django.utils.safestring import mark_safe
from .blocks import (
    NotebookBlock, ItemMenuBlock
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Site


class IndexPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['article_list'] = context['self'].get_descendants().live().exact_type(ArticlePage)
        return context

    class Meta:
        verbose_name ='Indice'
        verbose_name_plural = 'Indices'


class ArticlePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField([
        ('paragraph', blocks.RichTextBlock(label='Editor de texto')),
        ('html', blocks.RawHTMLBlock(label='HTML')),
        ('md', MarkdownBlock(label='Markdown')),
        ('notebook', NotebookBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['article.IndexPage']
    subpage_types = []

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def get_context(self, request):
        context = super().get_context(request)
        site = Site.find_for_request(request)
        context['related_articles'] = ArticlePage.objects.in_site(site).live().exact_type(ArticlePage).order_by('?')[:3]
        return context


@register_snippet
class Menu(models.Model):
    site = models.ForeignKey(Site, null=True, on_delete=models.CASCADE)
    code = models.CharField('Codigo', max_length=10)
    items = StreamField([
        ('item', ItemMenuBlock())
    ], null=True, blank=True)

    panels = [
        FieldPanel('site'),
        FieldPanel('code'),
        StreamFieldPanel('items'),
    ]

    def __str__(self):
        return self.code
