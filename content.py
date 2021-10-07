from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock, RichTextBlock, TextBlock)
from wagtail.images.blocks import ImageChooserBlock


class ActionCallLinkBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=False, help_text='Text to be used for the button')
    url = blocks.URLBlock(help_text='Link URL')

    class Meta:
        template = 'report/includes/content.action-button.link.html'
        icon = 'fa-external-link'


class PageTitleBlock(blocks.StructBlock):
    '''	StreamField block used to render page titles <h1>
    '''
    subtitle = blocks.CharBlock(required=True, min_length=1, max_length=2048,
                                help_text='Title of the page, rendered as an h1 tag')

    class Meta:
        template = 'report/includes/content.page-title.html'


class LinkBlock(blocks.StructBlock):
    '''	StreamField block used to render page titles <h1>
    '''
    name = blocks.CharBlock(required=True, min_length=1, max_length=100)
    id = blocks.CharBlock(required=True, max_length=100)

    class Meta:
        template = 'report/includes/content.link-block.html'


class FrontCoverBlock(blocks.StructBlock):
    ''' Cover block which provides a background here image and two content sections.
    '''
    cover_image = ImageChooserBlock(icon='picture',
                              help_text='Image to be used for the background of the cover block')
    logo = ImageChooserBlock(icon='picture')
    title = CharBlock()
    links = blocks.StreamBlock([
        ('link', LinkBlock())
    ])

    class Meta:
        template = 'report/includes/front-cover.html'


class ColumnsContent(blocks.StructBlock):
    # background_image = ImageChooserBlock(icon='picture')
    text = blocks.RichTextBlock()

    class Meta:
        template = 'report/includes/columns-content.html'


class ExecutiveSummaryBlock(blocks.StructBlock):
    # Block for creating a executive summary
    title = RichTextBlock()
    content = TextBlock()

    class Meta:
        template = 'report/includes/executive-summary.html'


class AcornColumnBaseBlock(blocks.StreamBlock):
    '''	Container block that is able to add a column of child blocks of different types
    '''
    column_class = 'col-sm-12 col-md-auto'

    def __init__(self, *args, **kwargs):
        # Add a column class to allow for clean override of the type of column in the template
        self.column_class = kwargs.pop('column_class', self.column_class)
        super(AcornColumnBaseBlock, self).__init__(*args, **kwargs)


class ThesesBlock(blocks.StructBlock):
    title = TextBlock()
    subtitle = TextBlock()

    class Meta:
        template = 'report/includes/content.theses.html'


class CircleImageBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=False)
    image = ImageChooserBlock(required=False)
    background_color = CharBlock()

    class Meta:
        template = 'report/includes/content.circle_image.html'


class ColumnBlock(AcornColumnBaseBlock):
    ''' Container block that is able to add a column of child blocks of different types
    '''
    text = blocks.RichTextBlock(icon='pilcrow',
                                features=[
                                    'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link',
                                    'document-link', 'image', 'embed', 'code', 'superscript', 'subscript',
                                    'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'])
    logo_and_circle_image = CircleImageBlock()
    person_name = RichTextBlock()
    short_description = RichTextBlock(template='report/includes/content.short_description.html')
    action_button = ActionCallLinkBlock()
    collage = blocks.ListBlock(ImageChooserBlock())
    theses = ThesesBlock()

    class Meta:
        template = 'report/includes/content.column.html'
        icon = 'fa-columns'


class ColumnsBlock(blocks.StreamBlock):
    ''' Container block that is able to hold multiple columns of child blocks of different types
    '''
    text = blocks.RichTextBlock(icon='pilcrow',
                                features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr',
                                          'link',
                                          'document-link', 'image', 'embed',
                                          'code', 'superscript', 'subscript', 'blockquote'])
    image = ImageChooserBlock()
    column = ColumnBlock(icon='fa-columns')
    column3 = ColumnBlock(column_class='col-sm-12 col-md-3')
    column4 = ColumnBlock(column_class='col-sm-12 col-md-4')
    column6 = ColumnBlock(column_class='col-sm-12 col-md-12 col-lg-6')
    column8 = ColumnBlock(column_class='col-sm-12 col-md-8')
    column9 = ColumnBlock(column_class='col-sm-12 col-md-9')

    class Meta:
        template = 'report/includes/content.columns.html'
        icon = 'fa-columns'


class DynamicBackgroundContentBlock(blocks.StreamBlock):
    '''	StreamField block that can be used to add content to parallax background blocks
    '''
    text = RichTextBlock(
        required=False,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link',
                  'image', 'embed',
                  'code', 'superscript', 'subscript', 'blockquote'])
    columns = ColumnsBlock()


class BackgroundImageBlock(blocks.StructBlock):
    '''	Cover image block with content in the foreground.
    '''
    image = ImageChooserBlock(icon='picture')
    content = DynamicBackgroundContentBlock(
        required=False, help_text='Web content displayed in the foreground (optional)')

    class Meta:
        icon = 'image'
        template = 'report/includes/content.background.image.html'


class CaseStudiesBlock(blocks.StructBlock):
    class Meta:
        icon = 'fa-bars'
        template = 'report/includes/case-studies.html'


class GlobalImpactsBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    content = RichTextBlock()
    countries = RichTextBlock()

    class Meta:
        icon = 'image'
        template = 'report/includes/global-impacts.html'


class GlobalImpactsEarthBlock(blocks.StructBlock):
    title = RichTextBlock()
    content_color = RichTextBlock()
    content = RichTextBlock()

    class Meta:
        icon = 'image'
        template = 'report/includes/global-impacts-earth.html'

