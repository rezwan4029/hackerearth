from django.db import models
import re

# Create your models here.

class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'pages'

    def __unicode__(self):
        return self.name


    def get_url_pattern_regex(self, urlpattern,
                              _param_matcher =re.compile(r':[^/]+',flags=re.UNICODE),
                              _param_replacement=lambda match: r'(?P<%s>[^/]+)' % match.group()[1:],
                              _cache={}):
        compiled_regex=_cache.get(urlpattern)
        if compiled_regex is None:
            if urlpattern.endswith('/'):
                urlpattern=urlpattern[:-1]

            #index should be entirely optional and match only digits
            if urlpattern.endswith('/:index'):
                urlpattern=urlpattern[:-7]+'/?(?P<index>\d*)'
                _param_replacement=lambda match:r'(?P<%s>[^/]*)' % match.group()[1:]

            regex=r'^%s/?$' % _param_matcher.sub(_param_replacement, urlpattern)
            compiled_regex=re.compile(regex,flags=re.UNICODE)
            _cache[urlpattern]=compiled_regex

        return compiled_regex


    def match_url(self, url):
        #this is to match btn two urls
        #self.url is the implicit url
        #url is the parameter url
        match = self.get_url_pattern_regex(self.url).match(url)
        if match:
            return True, match.groupdict()

        return False, {}


    @staticmethod
    def get_current_page(url):
        pages= Page.objects.all()
        for page in pages:
            matched, params = page.match_url(url)
            if matched:
                return page, params
        return None, {}


    def get_pages(self):
        #this is to get the list of all the pages from the db
        return list(self.pages.all())
