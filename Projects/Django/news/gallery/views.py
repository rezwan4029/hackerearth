from django.shortcuts import render
from gallery.models import Gallery
from news.API import NewscredApi

# Create your views here.

def render(request, page=1):
    ## galleris = to get the all galleries by using Gallery model class . .query
    try:
        gallery = Gallery.objects.filter(page_id=page)[0]
    except IndexError:
        return False

    options = {}

    query = gallery.query
    to_date = gallery.to_date
    from_date = gallery.from_date
    page_size = gallery.page_size

    if query:
        options['query'] = query
    if to_date:
        options['to_date'] =to_date
    if from_date:
        options['from_date'] =from_date
    if page_size:
        options['pagesize'] =page_size

    gallery_obj = NewscredApi('images', options)
    return gallery_obj.response()