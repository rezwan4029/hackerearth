from django.shortcuts import render
from topic.models import Topic
from newspapers.API import NewscredApi

# Create your views here.

def render(request, page=1):
    ## galleris = to get the all galleries by using Gallery model class . .query
    try:
        topic = Topic.objects.filter(page_id=page)[0]
    except IndexError:
        return False
    options = {}

    query = topic.query
    pagesize = topic.pagesize

    if query:
        options['query'] = query
    if pagesize:
        options['pagesize'] = pagesize

    article_obj = NewscredApi('topics', options)
    return article_obj.response()