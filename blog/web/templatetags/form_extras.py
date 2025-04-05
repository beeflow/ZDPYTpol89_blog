"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter
def as_bootstrap(form) -> str:
    html: str = ""

    for visible_field in form.visible_fields():
        css_class = "form-control"

        if visible_field.errors:
            css_class += " is_invalid"

        existing_class: str = visible_field.field.widget.attrs.get('class', '')
        visible_field.field.widget.attrs['class'] = f'{existing_class} {css_class}'.strip()

        html += f"""
            <div class="md-3">
                {visible_field.label_tag(attrs={"class": "form-label"})}
                {visible_field}
                {visible_field.errors.as_ul()}
                <div class="form-text">{visible_field.help_text}</div>
            </div>
        """

    return mark_safe(html)