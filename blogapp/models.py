from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.title), filname])


class Blog(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    date_published = models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=True, null=True ,upload_to=upload_path)


    def __str__(self):
        return self.title