import time
import logging


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.get_full_path()}")
        response = self.get_response(request)
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Response: {response.status_code} | Duration: {duration}")
        return response
    
    