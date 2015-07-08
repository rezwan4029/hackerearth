from django.shortcuts import render

from video.models import Video
from news.API import NewscredApi
# Create your views here.

def render(request,page=1):

    try:
        video = Video.objects.filter(page_id=page)[0]
    except IndexError:
        return False
    options = {}

    query = video.query
    to_date = video.to_date
    from_date = video.from_date
    page_size = video.page_size

    if query:
        options['query'] = query
    if to_date:
        options['to_date'] =to_date
    if from_date:
        options['from_date'] =from_date
    if page_size:
        options['pagesize'] = page_size

    video_obj = NewscredApi('videos', options)

    return video_obj.response()