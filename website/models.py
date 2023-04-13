from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('Family', 'Family'),
    ('Company', 'Company'),
    ('Couple', 'Couple'),
    ('Friend', 'Friend'),
    ('CarAccident', 'CarAccident'),
    ('Product', 'Product'),
)

class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Family')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recommend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommends')
    

class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='replies')

class Photo(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, null=True)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, null=True)




