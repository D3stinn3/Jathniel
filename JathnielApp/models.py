from django.db import models
from embed_video.fields import EmbedVideoField

class Videos(models.Model):
    video = EmbedVideoField()
    
    def __str__(self) -> str:
        return self.video
    
class Comments(models.Model):
    name = models.CharField(max_length=255, editable=True, null=True)
    email = models.EmailField(unique=True, null=True)
    mobile = models.PositiveIntegerField(null=True)
    message = models.TextField(max_length=500, editable=True, null=True)
    
    def __str__(self):
        return self.message