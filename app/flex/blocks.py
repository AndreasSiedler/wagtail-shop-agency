""" All blocks """
from wagtail.core.blocks import StructBlock, CharBlock, TextBlock, ListBlock, RawHTMLBlock, IntegerBlock, BooleanBlock
from wagtail.images.blocks import ImageChooserBlock


# Heading Section
class PageHeadingSectionBlock(StructBlock):
    """ Section Base Block - Ued by each section """
    heading = CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Sect',
    )

    class Meta:
        """ Meta data """
        template = 'blocks/page_heading_section.html'
        label = 'Page Heading Section'


# Hero Section Block

class HeroSectionBlock(StructBlock):
    """ Section Base Block - Ued by each section """
    heading = CharBlock(
        required=False,
        max_length=80,
        label='Feature',
        default='Super Awesome Feature',
    )
    subheading = CharBlock(
        required=False,
        max_length=100,
        label='Subheading',
        default='Super Awesome Hero Subheading',
    )
    description = TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    button = CharBlock(
        required=False,
        max_length=20,
        label='Button text',
        default='Get in touch',
    )
    image = ImageChooserBlock(
        required=False,
        label='Image',
    )

    class Meta:
        """ Meta data """
        template = 'blocks/hero_section.html'
        label = 'Hero Section'


# Logo Cloud Blocks

class LogoCloudBlock(StructBlock):
    """ LogoCloud Block """
    logos = ListBlock(
        StructBlock([
            ("image", ImageChooserBlock(required=True)),
        ])
    )

    class Meta:
        """ Meta data """
        template = 'blocks/logo_cloud.html'
        label = 'Logo Cloud'


# Service Section Block

class ServiceSectionBlock(StructBlock):
    """ Service Section Block """
    heading = CharBlock(required=True, max_length=100, label="Title")
    services = ListBlock(
        StructBlock([
            ("logo", RawHTMLBlock(required=True)),
            ("heading", CharBlock(required=True, max_length=100)),
            ("description", TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/service_section.html'
        label = 'Service Section'


# Feature Section Block

class FeatureSectionBlock(StructBlock):
    """ Feature Section Block """
    heading = CharBlock(required=True, max_length=100, label="Title")
    features = ListBlock(
        StructBlock([
            ("icon", RawHTMLBlock(required=True, rows=5)),
            ("heading", CharBlock(required=True, max_length=100)),
            ("description", TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/feature_section.html'
        label = 'Feature Section'

# Counter Section Block


class CounterSectionBlock(StructBlock):
    """ Counter Section Block """
    heading = CharBlock(required=True, max_length=100, label="Title")
    counters = ListBlock(
        StructBlock([
            ("heading", TextBlock(required=True, max_length=300)),
            ("count", IntegerBlock(required=True, max_value=1000000, )),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/counter_section.html'
        label = 'Counter Section'


# CTA Section
class CTASection(StructBlock):
    """ CTA Section Block """
    heading = CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Product',
    )
    description = TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    button = CharBlock(
        required=False,
        max_length=20,
        label='Button text',
        default='Get in touch',
    )

    class Meta:
        """ meta data """
        template = 'blocks/cta_section.html'
        label = 'CTA Section'


# Pricing Section
class PricingSectionBlock(StructBlock):
    """ Pricing Section Block """
    heading = CharBlock(required=True, max_length=100, label="Title")
    pricings = ListBlock(
        StructBlock([
            ("heading", TextBlock(required=True, max_length=300)),
            ("price", IntegerBlock(required=True, max_value=100000)),
            ("storage", IntegerBlock(required=True, max_value=100000)),
            ("hosting", BooleanBlock(required=False)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/pricing_section.html'
        label = 'Pricing Section'
