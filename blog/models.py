from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]
    

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        
        super(Post, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post-details', args=[self.slug])



class Comment(models.Model):

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        constraints =[UniqueConstraint(fields=['email','post'], name='unique_email_post')

        ]
        ordering =['created_on']
    

    
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
    



