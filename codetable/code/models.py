from django.db import models
from django.utils import timezone

from codetable.lib.utils import id_generator
from codetable.hackerearth.parameters import SupportedLanguages
from codetable.responselog.models import ResponseLog


class Code(models.Model):

    DEFAULT_CODE = '''#include <stdio.h>\n\nint main() {\n    printf("Hello World!");\n    return 0;\n}\n'''''

    id = models.CharField(max_length=6, primary_key=True, default=id_generator, editable=False)
    code = models.TextField(default=DEFAULT_CODE)
    input_stdin = models.TextField(null=True)
    language = models.CharField(max_length=30, default=SupportedLanguages.C)
    run_count = models.IntegerField(default=0)
    response = models.ForeignKey(ResponseLog, null=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<Code %r>" % self.id

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Code, self).save(args, kwargs)

    class Meta:
        db_table = 'codetable_code'

    def update(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Code, self).update(args, kwargs)
