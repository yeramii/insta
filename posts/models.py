from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    image = ProcessedImageField(upload_to='image/',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 100})
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)