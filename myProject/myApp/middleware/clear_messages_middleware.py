# myApp/middleware/clear_messages_middleware.py

from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin

class ClearMessagesMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        storage = messages.get_messages(request)
        list(storage)  # Access all messages to mark them as seen
        return response
