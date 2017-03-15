import datetime
from django.db import models
from django_mysql.models import SizedTextField, ListCharField

class article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique =True)
    body = SizedTextField(3)
    publisher = models.CharField(max_length=15)
    #tags for searching
    tags = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length = (6*11)
    )
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.body
    
    # TO CHECK IF ARTICLE PUBLISHED RECENTLY 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)