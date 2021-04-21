from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
import requests
import nbformat
from nbconvert import HTMLExporter

#class GridBlock(blocks.ListBlock):
#    any = AnyBlock()
#
#    class Meta:
#        template='blocks/grid.html'



class NotebookStructValue(blocks.StructValue):

    def html(self):
        ipynb = self.get('ipynb')
        if ipynb:
            notebook = nbformat.reads(ipynb, as_version=4)
            html_exporter = HTMLExporter()
            html_exporter.template_name = 'classic'
            (body, resources) = html_exporter.from_notebook_node(notebook)
            return body
        return ''


class NotebookBlock(blocks.StructBlock):
    show_code = blocks.BooleanBlock(default=True)
    url = blocks.URLBlock(required=False)
    ipynb = blocks.StaticBlock()

    class Meta:
        icon = 'site'
        value_class = NotebookStructValue

    def clean(self, value):
        for name, val in value.items():
            if name == 'url':
                req = requests.get(val)
                value['ipynb'] = req.text
        return super().clean(value)


class ItemMenuBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)
    new_window = blocks.BooleanBlock(default=False, required=False)
    label = blocks.CharBlock(required=False)
