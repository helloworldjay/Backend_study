from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50)
    posts = models.TextField()
    
    def __str__(self):
        return f"{self.author}|{self.posts[:10]}"

    def summary(self):
        return self.posts[:30]