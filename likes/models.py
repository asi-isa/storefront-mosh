from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# What object was liked by which user
class LikedItems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # we need to know the type(table) and the id of an object to identify it in our application
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # we assume that the id is a positive integer
    object_id = models.PositiveIntegerField()
    # actual object that this tag is applied to
    content_object = GenericForeignKey()
