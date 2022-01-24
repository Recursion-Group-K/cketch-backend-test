from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    ImageField,
    BooleanField,
    JSONField,
    DateTimeField,
    ForeignKey,
    CASCADE
)


class Drawing(Model):
    title = CharField(max_length=128)
    # image = ImageField()
    is_public = BooleanField(default=False)
    json_data = JSONField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    user = ForeignKey(User, related_name='drawings', on_delete=CASCADE)