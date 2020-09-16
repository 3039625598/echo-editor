from django.db import models
from django.utils.translation import gettext_lazy as _
from echo_editor.forms import EchoTextFormField

class EchoTextField(models.Field):
    description = _("Echo Text")

    def get_internal_type(self):
        return "EchoTextField"
    
    def to_python(self, value):
        if isinstance(value, str) or value is None:
            return value
        return str(value)
    
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return self.to_python(value)
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': EchoTextFormField
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
