
from wagtailmetadata.models import MetadataPageMixin

from flex.models import FlexPage


class HomePage(MetadataPageMixin, FlexPage):
    """
    HomePage model which inherits from Flexpage
    Hint: Here the home template is used which extends the flex_page template
    """
    subpage_types = ['blog.BlogIndexPage', 'form.FormPage']
