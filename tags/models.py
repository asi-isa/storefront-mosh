from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return self.select_related("tag").filter(
            content_type=content_type, object_id=obj_id
        )


class Tag(models.Model):
    label = models.CharField(max_length=255)


# What tag is applied to what item?
class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need to know the type(table) and the id of an object to identify it in our application
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # we assume that the id is a positive integer
    object_id = models.PositiveIntegerField()
    # actual object that this tag is applied to
    content_object = GenericForeignKey()
