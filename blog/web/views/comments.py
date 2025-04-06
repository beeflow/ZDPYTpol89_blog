"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from web.models import Comment, Post


class CommentsListView(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'

    def get(self, request, post_pk, *args, **kwargs):
        self.queryset = self.model.objects.filter(post_id=post_pk)

        return super().get(request, *args, **kwargs)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment/comment_form.html'
    fields = ('content', 'author')

    def get(self, request, post_id, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(pk=post_id)
        form = self.get_form()

        # @todo sprawdzić jak na tym etapie dodać post do komentarza (formularza)
        form.data['post'] = post

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)


    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post_id})
