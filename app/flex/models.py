""" Flex Page """

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import ListBlock

from wagtailmetadata.models import MetadataPageMixin

from .blocks import (PageHeadingSectionBlock, HeroSectionBlock, LogoCloudBlock, ServiceSectionBlock,
                     FeatureSectionBlock, CounterSectionBlock, CTASection, PricingSectionBlock)


# Create your models here.


class FlexPage(Page):
    """
    Abstract Page Extension
    Define abstract to dont create own database table for this model - fields are created in the child class
    """
    content = StreamField(
        [
            ('page_heading_section_block', PageHeadingSectionBlock()),
            ('hero_section_block', HeroSectionBlock()),
            ('logo_cloud_block', LogoCloudBlock()),
            ('service_section_block', ServiceSectionBlock()),
            ('feature_section_block', FeatureSectionBlock()),
            ('counter_section_block', CounterSectionBlock()),
            ('cta_section_block', CTASection()),
            ('pricing_section_block', PricingSectionBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    template = "flex/flex_page.html"

    class Meta:
        abstract = True
