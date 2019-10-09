from django.urls import path
from creategoogleform.api.google_form import CreateForm, GetUserDetail, UpdateDeleteUserDetail

urlpatterns = [
                path("create-google-form/", CreateForm.as_view(), name="create_google_form"),
                path("get-users-google-form/", GetUserDetail.as_view(), name="get_users_google_form"),
                path("update-user/<uuid:id>/", UpdateDeleteUserDetail.as_view(), name="update_user_google_form"),
                path("delete-user/<uuid:id>/", UpdateDeleteUserDetail.as_view(), name="delete_user_google_form"),

            ]
