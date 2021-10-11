from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.models import Image

from .content import PageTitleBlock, FrontCoverBlock, ColumnsContent, ExecutiveSummaryBlock, BackgroundImageBlock, \
    ColumnsBlock, CaseStudiesBlock, GlobalImpactsEarthBlock, GlobalImpactsBlock, InNumbersBlock, \
    ScholarshipsTimelineBlock, FocusMalawiBlock, BackgroundImageMalawiBlock



class ReportPage(Page):
    '''	Start page
    '''
    body = StreamField([
        ('text', RichTextBlock(icon='pilcrow',
                               features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr',
                                         'link', 'document-link', 'image', 'embed',
                                         'code', 'superscript', 'subscript', 'blockquote'])),
        ('front_cover', FrontCoverBlock()),
        ('columns_content', ColumnsContent()),
        ('executive_summary', ExecutiveSummaryBlock()),
        ('fullwidth_background_image', BackgroundImageBlock()),
        ('case_study', CaseStudiesBlock()),
        ('global_impacts_earth', GlobalImpactsEarthBlock()),
        ('global_impacts', GlobalImpactsBlock()),
        ('in_numbers_image', InNumbersBlock()),
        ('columns', ColumnsBlock(template='report/includes/content.columns.block.html')),
        ('scholarship_timeline', ScholarshipsTimelineBlock()),
        ('focus_malawi', FocusMalawiBlock()),
        ('background_malawi', BackgroundImageMalawiBlock()),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'report/report-page.html'

    # subpage_types = ['report.CaseStudyPage', 'report.CaseStudyListPage']

    def get_context(self, request):
        context = super().get_context(request)
        case_study_list = self.get_children().type(CaseStudyListPage).first()
        if case_study_list:
            context["case_studies"] = CaseStudyPage.objects.filter(featured=True).specific()
        return context


class CaseStudyListPage(Page):
    ''' Case study list page
    '''
    body = StreamField([
        ('text', RichTextBlock(icon='pilcrow',
                               features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr',
                                         'link', 'document-link', 'image', 'embed',
                                         'code', 'superscript', 'subscript', 'blockquote'])),
        ('columns_content', ColumnsContent()),
        ('case_study', CaseStudiesBlock()),
        ('columns', ColumnsBlock(template='report/includes/content.columns.block.html')),
    ], null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'report/case-study-list-page.html'

    subpage_types = ['report.CaseStudyPage']

    def get_context(self, request):
        context = super().get_context(request)
        context["case_studies"] = self.get_children().type(CaseStudyPage).specific()
        return context


class CaseStudyPage(Page):
    '''	Case Study page
    '''
    body = StreamField([
        ('columns', ColumnsBlock(template='report/includes/case-study.columns.block.html')),
    ], null=True)

    background_color = models.CharField(max_length=10, blank=True, null=True,
        help_text='Background color that should be used for the model viewer.')
    person_name = models.CharField(max_length=1000, null=True, blank=True,
        help_text="Title of the case study")
    description = models.CharField(max_length=2000, null=True, blank=True,
        help_text="Description of the case study")
    cover = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                              help_text='Image to be shown in the header of case study')
    featured = models.BooleanField(default=True)

    template = 'report/case-study-page.html'

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    settings_panels = Page.settings_panels + [
        MultiFieldPanel([
            FieldPanel('background_color'),
            FieldPanel('person_name'),
            FieldPanel('description'),
            FieldPanel('featured'),
            ImageChooserPanel('cover')
        ], "Meta"),
    ]

