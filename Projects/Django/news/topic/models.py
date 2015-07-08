from django.db import models
from pages.models import Page

# Create your models here.

class Topic(models.Model):
    page_id = models.ForeignKey(Page)
    name=models.CharField(max_length=255)
    query = models.CharField( max_length =  255)
    pagesize = models.IntegerField()

    class Meta:
        db_table = 'topics'

    def __unicode__(self):
        return self.name