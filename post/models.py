from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created', auto_now=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    content = models.TextField(max_length=191)
    is_active = models.BooleanField(default=True)

    def __str__ (self):
        return 'Post: {}'.format(self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    date_created = models.DateTimeField('date created', auto_now=True)
    content = models.TextField(max_length=191)

    def __str__ (self):
        return 'Comment: {}'.format(self.content)
