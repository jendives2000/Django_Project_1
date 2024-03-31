# the app of this model (tags) is meant to be usable with any other app. So it is independent.
# in other words, it creates generic relationships.
# This is why we use the default app contenttype (#1).

# NOTE:
# !! This will NOT work with GUID type ID because they are not integers.

from django.db import models
from django.contrib.contenttypes.models import ContentType  # 1
from django.contrib.contenttypes.fields import GenericForeignKey  # 3


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # get what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # We can identify any object from any app (record from any DB) with these 2: Type, ID
    # Type: could be anything: product, video, article, etc.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 1
    # ID:
    object_id = models.PositiveIntegerField()  # !! see NOTE above
    # get the actual product or object name
    actual_object = GenericForeignKey()  # 3
