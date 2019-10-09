from creategoogleform.views import BaseCreateGet, BaseUpdateDelete
from creategoogleform.api.schema import CreateGoogleFormSchema, GetUserDetailSchema, UpdateUserSchema
from django.http import JsonResponse
from creategoogleform.models import UserDetailModel
from creategoogleform.http_tools import build_response_dict
from creategoogleform import api_exception


class CreateForm(BaseCreateGet):
    """
        Register user view class.
    """
    schema_class = CreateGoogleFormSchema
    model = UserDetailModel

    def post(self, request, *args, **kwargs):
        """
        Endpoint: /googleform/create-google-form/
        @apiheader
        Content-Type application/json
        @Body
        {
            "name": "rishi",
            "email": "rishik@gmail.com",
            "gender": "Male",
            "skill": "C++"
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        obj = self.model.objects.create(**self.req_data)
        response_dict = build_response_dict(
            response_type="POST",
            response_text="User information registered successfully",
            id={"user_id": str(obj.id)},
        )
        return JsonResponse(self.make_response(data=response_dict), status=201)

class GetUserDetail(BaseCreateGet):
    """
        Get all users, those are registered themselves.
    """

    schema_class = GetUserDetailSchema
    model = UserDetailModel
    def get(self, request, *args, **kwargs):
        """
        Endpoint: /googleform/get-users-google-form/
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        users = []
        obj = self.model.objects.all()
        for user in obj:
            users.append(
                {
                    "User_Id": str(user.id),
                    "Name": str(user.name),
                    "Email": str(user.email),
                    "Gender": str(user.gender),
                    "Skills": str(user.skill)
                }
            )

        response_dict = build_response_dict(
            response_type="GET",
            response_text="User information extracted successfully",
            response_data=users
        )
        return JsonResponse(self.make_response(data=response_dict), status=200)

class UpdateDeleteUserDetail(BaseUpdateDelete):
    """
        Update user detail view class.
    """
    schema_class = UpdateUserSchema
    model = UserDetailModel

    def put(self, request, id, *args, **kwargs):
        """
        Endpoint: /googleform/update-user/<user_id>/
        :param request:
        :param id:
        :param args:
        :param kwargs:
        :return:
        """
        obj = self.model.objects.filter(id=id)
        if not obj:
            raise api_exception.BadRequestData(errors="id doesn't exist.")
        self.model().update_fields(obj[0], **self.req_data)
        response_dict = build_response_dict(
            response_type="PUT", response_text="User information has been successfully updated."
        )
        return JsonResponse(self.make_response(response_dict), status=202)

    def delete(self, request, id, *args, **kwargs):
        """
        Endpoint: /googleform/delete-user/<user_id>/
        :param request:
        :param id:
        :param args:
        :param kwargs:
        :return:
        """
        obj = self.model.objects.filter(id=id)
        if not obj:
            raise api_exception.BadRequestData(errors="id doesn't exist.")
        self.model().delete_obj(obj)
        response_dict = build_response_dict(
            response_type="DELETE", response_text="User information has been successfully deleted."
        )
        return JsonResponse(self.make_response(response_dict), status=204)