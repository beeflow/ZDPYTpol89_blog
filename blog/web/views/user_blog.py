"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from web.models import Post

User = get_user_model()


class UserBlogView(ListView):
    model = Post

    def get(self, request, pk, *args, **kwargs):
        self.user = get_object_or_404(User, pk=pk)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context.update(
            {
                'title': f'Blog by: {self.user}',
                'blog_owner': self.user,
            }
        )

        return context
