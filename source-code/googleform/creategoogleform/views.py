import json
from django.views.generic import View
from creategoogleform import api_exception
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class BaseView(View):
    """
    Base class of view to make response and catching APIs error.
    """
    schema_class = None

    def __init__(self, *args, **kwargs):
        """
            Constructor. Called in the URLconf; can contain helpful extra
            keyword arguments, and other things.
        """
        super(BaseView, self).__init__(*args, **kwargs)

    def make_response(self, data):
        if isinstance(data, dict):
            return {"response": data, "meta": {}}
        else:
                raise api_exception.BadRequestData()

class BaseCreateGet(BaseView):
    """
        Base View class to create and get users.
    """

    @method_decorator(api_exception.api_exception_handler)
    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        self.schema = self.schema_class()
        errors = None

        if request.method == "GET":
            self.req_params, errors = self.schema.load(request.GET)

        # check schema for POST request
        elif request.method == "POST":
            if not request.body:
                raise api_exception.BadRequestData()

            elif isinstance(json.loads(request.body), list):
                self.schema = self.schema_class(many=True)
            else:
                pass
            self.req_data, errors = self.schema.loads(request.body)
        else:
            raise api_exception.MethodNotAllowed(request.method)

        # schema errors to be captured here
        if errors:
            raise api_exception.BadRequestData(errors=errors)

        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise api_exception.NotImplemented()

    def post(self, request, *args, **kwargs):
        raise api_exception.NotImplemented()


class BaseUpdateDelete(BaseView):
    """
        Base View class to update and delete user.
    """

    @method_decorator(api_exception.api_exception_handler)
    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        self.schema = self.schema_class()
        errors = None
        if request.method == "PUT":
            if not request.body:
                raise api_exception.BadRequestData(errors="No request data for edit")
            self.req_data, errors = self.schema.loads(request.body)
        if errors:
            raise api_exception.BadRequestData(errors=errors)
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def put(self, request, id, *args, **kwargs):
        raise api_exception.NotImplemented()

    def patch(self, request, *args, **kwargs):
        raise api_exception.NotImplemented()

    def delete(self, request, id, *args, **kwargs):
        raise api_exception.NotImplemented()
