import logging

from django.http import HttpResponseNotFound
from django.template.loader import render_to_string

# Set up a logger for capturing 404 warnings
logger = logging.getLogger('django.request')


class Handle404Middleware:
    """
    Custom middleware that intercepts 404 (Not Found) responses,
    logs the missing path, and renders a styled HTML error page.
    """

    def __init__(self, get_response):
        # This function will be called for each request
        self.get_response = get_response

    def __call__(self, request):
        # Proceed with the standard request-response cycle
        response = self.get_response(request)

        # If the response is not a 404, return it as is
        if response.status_code != 404:
            return response

        # Log the missing URL path for debugging or monitoring purposes
        logger.warning(f"Oooooooooo, co to: 404 Not found: {request.path}")

        # Render a custom 404 page from template
        html = render_to_string('globals/404.html')

        # Return a properly marked 404 response with the rendered content
        return HttpResponseNotFound(html)
