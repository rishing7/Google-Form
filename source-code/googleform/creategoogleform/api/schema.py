from marshmallow import Schema, fields, validates, ValidationError, validates_schema
from creategoogleform.models import UserDetailModel


class GoogleFormBaseSchema(Schema):
    """
        Base class schema for user detail validation.
    """
    name = fields.Str(required=False)
    email = fields.Email(required=True)
    gender = fields.Str(required=False)
    skill = fields.Str(required=False)

    @validates("name")
    def validate_name(self, value):
        if not value:
            raise ValidationError("Enter valid name.")
        return value.strip()

    @validates("gender")
    def validate_gender(self, value):
        if value not in ["Male", "Female"]:
            raise ValidationError("Enter valid gender such as Male or Female.")
        return value

    @validates("email")
    def validate_email(self, value):
        obj = UserDetailModel.objects.filter(email=value)
        if obj:
            raise ValidationError("Email already exists.")


class CreateGoogleFormSchema(GoogleFormBaseSchema):
    """
    Schema class to validate fields.
    """
    pass


class GetUserDetailSchema(Schema):
    id = fields.UUID(required=False)

class UpdateUserSchema(GoogleFormBaseSchema):
    """
    Update user detail schema.
    """
    pass
