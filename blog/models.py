from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid

# Create your models here.

class Post(models.Model):
    STATUS_OF_POST = [
        ('DF','DRAFT'),('PB','PUBLISHED'),
    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_OF_POST, default='DF')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]
    

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        
        super(Post, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title


