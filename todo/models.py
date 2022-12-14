from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User,null = True,on_delete = models.CASCADE,blank=True)
    title = models.CharField(max_length=100,null = True)
    description = models.TextField(null = True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

