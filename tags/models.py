from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


# What tag is applied to what item?
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need to know the type(table) and the id of an object to identify it in our application
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # we assume that the id is a positive integer
    object_id = models.PositiveIntegerField()
    # actual object that this tag is applied to
    content_object = GenericForeignKey()
