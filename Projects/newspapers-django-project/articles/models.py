from django.db import models
from pages.models import Page
from newspapers.settings import ARTICLE_CHOICES

# Create your models here.

class Article(models.Model):
    page_id = models.ForeignKey(Page)
    name=models.CharField(max_length=255)
    block_choice = models.CharField(max_length=25,choices=ARTICLE_CHOICES)
    query = models.CharField( max_length= 25)
    from_date = models.DateTimeField( null= True, blank= True)
    to_date = models.DateTimeField(null= True, blank= True)
    page_size = models.IntegerField( null= True, blank= True)
    has_images= models.BooleanField()

    class Meta:
        db_table = 'articles'

    def __unicode__(self):
        return self.name