from tortoise import fields, models
import datetime as dt

class BaseModel(models.Model):
    """Base model"""
    id: int =  fields.IntField(pk=True)
    created_at: dt.datetime = fields.DatetimeField(auto_now_add=True)

class User(BaseModel):
    """User of the app."""
    name: str = fields.CharField(max_length=255)
    username: str = fields.CharField(max_length=255, unique=True)
    password: str = fields.CharField(max_length=255)






