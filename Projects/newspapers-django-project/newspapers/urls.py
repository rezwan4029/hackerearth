from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^articles/[A-Za-z]+/[0-9]+$','articles.views.response_article'  ),
    #
    #url(r'^gallery/[A-Za-z]+/[0-9]+$','gallery.views.response_gallery'  ),
    #
    #url(r'^images/[A-Za-z]+/[0-9]+$','images.views.response_images'  ),
    #
    #url(r'^videos/[A-Za-z]+/[0-9]+$','video.views.response_video'  ),
    url(r'^', 'pages.views.home', name='home'),
)
