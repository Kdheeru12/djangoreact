from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    categories=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.categories
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    categories = models.ForeignKey(Categories,blank=True,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-timestamp",)

def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug 
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver,sender=Blog)
