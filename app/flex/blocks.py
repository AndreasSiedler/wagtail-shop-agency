""" All blocks """
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


# Heading Section
class PageHeadingSectionBlock(blocks.StructBlock):
    """ Section Base Block - Ued by each section """
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Section',
    )

    class Meta:
        """ Meta data """
        template = 'blocks/page_heading_section.html'
        label = 'Page Heading Section'


# Content Seciton Block
class ContentSectionBlock(blocks.StructBlock):
    """ Section Base Block - Ued by each section """
    layout = blocks.ChoiceBlock(
        choices=(
            ('centered', 'Centered'),
            ('two_columns_with_image', 'Two columns with image')
        )
    )
    content = blocks.RichTextBlock(
        required=False,
        max_length=10000,
        label='Content',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    image = ImageChooserBlock(required=False)

    class Meta:
        """ Meta data """
        template = 'blocks/content_section.html'
        label = 'Content Section'


# Hero Section Block
class HeroSectionBlock(blocks.StructBlock):
    """ Section Base Block - Ued by each section """
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Feature',
        default='Super Awesome Feature',
    )
    subheading = blocks.CharBlock(
        required=False,
        max_length=100,
        label='Subheading',
        default='Super Awesome Hero Subheading',
    )
    description = blocks.TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    button = blocks.CharBlock(
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

class LogoCloudBlock(blocks.StructBlock):
    """ LogoCloud Block """
    logos = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True, label="Image")),
        ])
    )

    class Meta:
        """ Meta data """
        template = 'blocks/logo_cloud.html'
        label = 'Logo Cloud'


# Service Section Block

class ServiceSectionBlock(blocks.StructBlock):
    """ Service Section Block """
    heading = blocks.CharBlock(required=True, max_length=100, label="Title")
    services = blocks.ListBlock(
        blocks.StructBlock([
            ("logo", blocks.RawHTMLBlock(required=True)),
            ("heading", blocks.CharBlock(required=True, max_length=100)),
            ("description", blocks.TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/service_section.html'
        label = 'Service Section'


# Feature Section Block

class FeatureSectionBlock(blocks.StructBlock):
    """ Feature Section Block """
    heading = blocks.CharBlock(required=True, max_length=100, label="Title")
    features = blocks.ListBlock(
        blocks.StructBlock([
            ("icon", blocks.RawHTMLBlock(required=True, rows=5)),
            ("heading", blocks.CharBlock(required=True, max_length=100)),
            ("description", blocks.TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/feature_section.html'
        label = 'Feature Section'

# Counter Section Block


class CounterSectionBlock(blocks.StructBlock):
    """ Counter Section Block """
    heading = blocks.CharBlock(required=True, max_length=100, label="Title")
    counters = blocks.ListBlock(
        blocks.StructBlock([
            ("heading", blocks.TextBlock(required=True, max_length=300)),
            ("count", blocks.IntegerBlock(required=True, max_value=1000000, )),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/counter_section.html'
        label = 'Counter Section'


# CTA Section
class CTASection(blocks.StructBlock):
    """ CTA Section Block """
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Product',
    )
    description = blocks.TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    button = blocks.CharBlock(
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
class PricingSectionBlock(blocks.StructBlock):
    """ Pricing Section Block """
    heading = blocks.CharBlock(required=True, max_length=100, label="Title")
    pricings = blocks.ListBlock(
        blocks.StructBlock([
            ("heading", blocks.TextBlock(required=True, max_length=300)),
            ("price", blocks.IntegerBlock(required=True, max_value=100000)),
            ("storage", blocks.IntegerBlock(required=True, max_value=100000)),
            ("hosting", blocks.BooleanBlock(required=False)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/pricing_section.html'
        label = 'Pricing Section'
