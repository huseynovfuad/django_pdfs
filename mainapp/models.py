from django.db import models

# Create your models here.

def upload_to(instance,filename):
    return "{}/{}".format('books',filename)

class Books(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(upload_to=upload_to)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitablar'