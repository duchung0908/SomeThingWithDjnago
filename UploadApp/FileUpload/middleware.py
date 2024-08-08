from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger('django.request')

class RequestResponseLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._request_start_time = datetime.now()
        request._body = request.body

    def process_response(self, request, response):
        # Calculate API latency
        api_latency = datetime.now() - request._request_start_time

        # Get request headers
        headers = {key.replace('HTTP_', '').replace('_', '-'): value for key, value in request.META.items() if key.startswith('HTTP_')}

        # Log the data
        logger.info({
            'data': {
                'api_endpoint': request.path,
                'api_method': request.method,
                'api_latency': str(api_latency),
                'api_status_code': response.status_code,
                'header': headers,
                'request': request.body.decode('utf-8') if request.method != 'GET' else None,
                'response': response.content.decode('utf-8') if response.status_code != 404 else None,
            }
        })

        return response
