from django.db import models
from django.utils import timezone


class ResponseLog(models.Model):
    id = models.IntegerField(primary_key=True)
    output_html = models.TextField()
    run_status = models.CharField(max_length=200, default='CE')
    memory_used = models.CharField(max_length=200, default='0.0')
    time_used = models.CharField(max_length=30, default='0.0')
    he_web_link = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return "ResponseLog(link:%s , time:%s , memory:%s )" % (self.he_web_link, self.time_used, self.memory_used)

    class Meta:
        db_table = 'codetable_responselog'
