from django.db import models
from posts.models import Post
from multiselectfield import MultiSelectField
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment_post',
        null=True
    )
    parent_comment = models.IntegerField(null=False, default=0)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

