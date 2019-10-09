from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    created_ts = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj

    @classmethod
    def delete_obj(cls, obj):
        obj.delete()

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self.id)

    def update_fields(self, obj, **kwargs):
        """ Update fields of given users object"""
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()

class UserDetailModel(BaseModel):
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=20, unique=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    skill = models.TextField(max_length=100, blank=True)
