from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#A custom manager to retrieve published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)
            

class Post(models.Model):
    
    class Status(models.TextChoices):
        #names|values|labels: choices
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        #actual value | human readable
        # STATUS_CHOICES = [
        #     (DRAFT, 'Draft'),
        #     (PUBLISHED, 'Published'),
        # ]
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)  #implies an Index by default
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                            related_name='blog_posts')  #a user caan write any number of posts:user.blog_posts
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  #the default manager
    published = PublishedManager()  #our custom manager
    
    class Meta:
        ordering = ['-publish']  #from newest to oldest: in descending order
        indexes = [
            models.Index(fields=['-publish']),
        ]  #to speed up our database query
    
    def __str__(self):
        return self.title
