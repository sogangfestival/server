from django.db import models
from posts.models import Post
# from multiselectfield import MultiSelectField
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment_post',
    )
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='cocomments',
        null=True,
        blank=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    writer = models.CharField(max_length=100)

    def __str__(self):
        return self.post.title