from django.views.generic import ListView

from web.models import Post


class WebView(ListView):
    template_name = 'index.html'
    model = Post
