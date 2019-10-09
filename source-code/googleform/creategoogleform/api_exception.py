from functools import wraps

from django.http import JsonResponse
from django.utils.encoding import force_text

# most exception classes are a blatant ripoff, just shaved off some stuff:
# https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/exceptions.py
# exception_handler is a homegrown decorator,
# different from how DRF handles it.


def api_exception_handler(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        try:
            return f(request, *args, **kwargs)
        except APIException as e:
            return JsonResponse({"message": str(e.detail), "error": e.errors, "status_code": e.code}, status=e.code)

    return decorated_function


class APIException(Exception):
    """
       Base class for API exceptions.
       Subclasses should provide `.status_code` and `.default_detail` properties.
       """

    # default - for unhandled exceptions - should ideally never happen, since
    # these will be mostly raised by devs themselves while handling requests.
    status_code = 500
    default_detail = "A server error occurred."

    def __init__(self, detail=None, errors=None, code=None):

        if detail is None:
            self.detail = self.default_detail
        else:
            self.detail = detail

        self.errors = errors

        if code is None:
            self.code = self.status_code
        else:
            self.code = code

    def __str__(self):
        return self.detail


class BadRequestData(APIException):
    status_code = 400
    default_detail = "Bad request data."


class ParseError(APIException):
    status_code = 400
    default_detail = "Malformed request."


class AuthenticationFailed(APIException):
    status_code = 401
    default_detail = "Incorrect authentication credentials."


class NotAuthenticated(APIException):
    status_code = 401
    default_detail = "Authentication credentials were not provided or failed."


class PermissionDenied(APIException):
    status_code = 403
    default_detail = "Permission error."


class NotFound(APIException):
    status_code = 404
    default_detail = "Not found."


class MethodNotAllowed(APIException):
    status_code = 405
    default_detail = 'Method "{method}" not allowed.'

    def __init__(self, method, detail=None):
        if detail is not None:
            self.detail = force_text(detail).format(method=method)
        else:
            self.detail = force_text(self.default_detail).format(method=method)
        super(MethodNotAllowed, self).__init__()


class NotAcceptable(APIException):
    status_code = 406
    default_detail = "Could not satisfy the request Accept header."


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = "The server is currently unable to handle the request, " "please try again later"


class NotImplemented(APIException):
    status_code = 501
    default_detail = "The server does not support the functionality " "required to fulfill the request"


class DuplicateResource(APIException):
    status_code = 409
    default_detail = "Resource already exists"


class ResourceInMutualExclusionZone(APIException):
    status_code = 409
    default_detail = "Read/Write not allowed on the resource"


class UnProcessableResource(APIException):
    status_code = 422
    default_detail = "Resource is an un-processable entity"


class ImproperlyConfigured(APIException):
    status_code = 500
    default_detail = "Improperly Configured"


class ValidationError(APIException):
    status_code = 400
    default_detail = "Bad Request"