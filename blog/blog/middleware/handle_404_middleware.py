import logging

from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponse
from django.template.loader import render_to_string

# Set up a logger for capturing 404 warnings
logger = logging.getLogger('django.request')


def response_404(request):
    # Log the missing URL path for debugging or monitoring purposes
    logger.warning(f"Oooooooooo, co to: 404 Not found: {request.path}")

    # Render a custom 404 page from template
    html = render_to_string('globals/404.html')

    # Return a properly marked 404 response with the rendered content
    return HttpResponseNotFound(html)


def response_500(request):
    html = render_to_string('globals/500.html')

    return HttpResponseServerError(html)


response_map: dict = {
    404: response_404,
    500: response_500,
}


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

        if 200 <= response.status_code < 400:
            return response

        return response_map.get(response.status_code, response_404)(request)
