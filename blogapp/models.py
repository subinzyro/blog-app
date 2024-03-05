from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=20)
    blog_name=models.CharField(max_length=30)
    description=models.TextField()
    # contact=models.CharField(max_length=15)
    class Meta:
        db_table="blog"
    def __str__(self):
        return f"{self.name} {self.blog_name}"