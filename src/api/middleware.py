from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self,request):
        logging.info("Client IP Address : "+str(request.META.get("REMOTE_ADDR")))
        logging.info("Request Method : "+str(request.META.get("REQUEST_METHOD")))
        logging.info("URL Requested : "+str(request.path))
        logging.info("Request Body Contents : "+str(request.body))
        logging.info("Host Name of Client : "+str(request.META.get("REMOTE_HOST")))
        logging.info("Host Name of Server : "+str(request.META.get("SERVER_NAME")))
        return None

    def process_response(self,request,response):
        logging.info("Response Content : "+str(response.content))
        logging.info("Response Code : "+str(response.status_code))
        return response