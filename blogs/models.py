from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    
    category = models.ForeignKey(CategoryModel, related_name='blogs')