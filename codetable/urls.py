from django.conf.urls import patterns, include, url
from django.contrib import admin

from codetable.code.views import CodeTableView, CodeTableEditor

admin.autodiscover()

urlpatterns = patterns(

    url(r'^?/$', CodeTableView.as_view(), name='code'),
    url(r'^code/(?P<code_id>.*)/$', CodeTableEditor.as_view(), name='codetable_editor'),
    url(r'^savecode/(?P<code_id>.*)/$', CodeTableView.as_view(), name='save_code'),
    url(r'^code?/$', CodeTableView.as_view(), name='code'),
    url(r'^admin/', include(admin.site.urls)),
)
