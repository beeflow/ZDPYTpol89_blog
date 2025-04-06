"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from typing import Optional

from django.urls import path
from django.utils.decorators import classonlymethod
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# @todo, dlaczego nie działa app_prefix w przypadku komentarzy???
class CustomCreateView(CreateView):
    app_prefix: Optional[str] = None

    def get_success_url(self) -> str:
        """Return the URL to redirect to after successful creation."""
        app_prefix = self.kwargs.get('app_prefix')
        return f"/{app_prefix}/{self.object.pk}" if app_prefix else f"/{self.object.pk}"


class CustomUpdateView(UpdateView):
    app_prefix: Optional[str] = None

    def get_success_url(self) -> str:
        """Return the URL to redirect to after successful creation."""
        app_prefix = self.kwargs.get('app_prefix')
        return f"/{app_prefix}/{self.object.pk}" if app_prefix else f"/{self.object.pk}"

# @todo - dołożyć obsługę parametru wejściowego "success_url" (jak w urls.py)
class HtmlViewSet:
    fields = None
    fields_by_view = {}
    template_names = {}

    model = None
    prefix = None
    template_prefix = None

    @classonlymethod
    def as_viewset(cls, **initkwargs) -> list:
        model = initkwargs.get('model')
        assert model is not None, "You must provide model"  # noqa

        fields = initkwargs.get('fields', [])
        prefix = initkwargs.get('prefix', '')
        template_names = initkwargs.get('template_names', {})
        fields_by_view = initkwargs.get('fields_by_view', {})

        model_name = model.__name__.lower()
        template_prefix = initkwargs.get('template_prefix', '') or model_name

        route_names = {
            "list": f"{prefix}",
            'create': f"{prefix}/add" if prefix else "add",
            'update': f"{prefix}/<pk>/update" if prefix else "<pk>/update",
            'delete': f"{prefix}/<pk>/delete" if prefix else "<pk>/delete",
            'detail': f"{prefix}/<pk>" if prefix else "<pk>",
        }

        return [
            path(
                route_names['list'],
                ListView.as_view(
                    model=model,
                    template_name=template_names.get('list') or f"{template_prefix}/{model_name}_list.html"
                ), name=f'{model_name}-list'
            ),
            path(
                route_names['create'],
                CustomCreateView.as_view(
                    model=model,
                    fields=list(fields) + list(fields_by_view.get('create', [])),
                    template_name=template_names.get('create') or f"{template_prefix}/{model_name}_form.html",
                    app_prefix=prefix,
                ), name=f'{model_name}-create'
            ),
            path(
                route_names['update'],
                CustomUpdateView.as_view(
                    model=model,
                    fields=list(fields) + list(fields_by_view.get('update', [])),
                    template_name=template_names.get('update') or f"{template_prefix}/{model_name}_form.html",
                    app_prefix=prefix,
                ), name=f'{model_name}-edit'
            ),
            path(
                route_names['delete'],
                DeleteView.as_view(
                    model=model,
                    template_name=template_names.get('delete') or f"{template_prefix}/{model_name}_confirm_delete.html",
                ), name=f'{model_name}-delete'
            ),
            path(
                route_names['detail'],
                DetailView.as_view(
                    model=model,
                    template_name=template_names.get('detail') or f"{template_prefix}/{model_name}_detail.html",
                ), name=f'{model_name}-detail'
            ),
        ]
