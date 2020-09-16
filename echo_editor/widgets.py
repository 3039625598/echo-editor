from django.forms import Widget
from django.utils import datetime_safe, formats

class EchoEditorWidget(Widget):
    template_name = 'echo_editor/editor.html'

    def __init__(self, attrs=None):
        # Use slightly better defaults than HTML's 20x2 box
        default_attrs = {'style': 'display:none;'}
        # default_attrs = {}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
