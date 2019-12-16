from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 256)
    slug = models.SlugField()
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default = 'default.png',blank=True)
    author= models.ForeignKey(User,default=None,on_delete=models.PROTECT)
    #add author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:300]+'....'

    def titleSnippet(self):
        return self.title[:50]+'..'
