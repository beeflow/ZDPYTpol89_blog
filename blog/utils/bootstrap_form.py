"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

def add_bootstrap_classes(form):
    for visible_field in form.visible_fields():
        existing_class: str = visible_field.field.widget.attrs.get('class', '')
        visible_field.field.widget.attrs['class'] = f'{existing_class} form-control'.strip()


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_bootstrap_classes(self)
