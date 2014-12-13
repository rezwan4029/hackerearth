from django.shortcuts import render

from articles.models import Article
from newspapers.API import *
# Create your views here.

#def render(request,page=1):
    #return Article.objects.filter(page_id=page)


ARTICLE_FIELDS = [
    'article.title',
    'article.guid',
    'article.description',
    'article.image.guid',
    'article.image.caption',
    'article.image.urls.large',
    'article.image.width',
    'article.image.height'
]


def render(request, page):

    articles = Article.objects.filter(page_id=page)
    options = {}
    results = {}
    for article in articles:
        query = article.query
        to_date = article.to_date
        from_date = article.from_date
        page_size = article.page_size
        has_images = article.has_images
        if query:
            options['query'] = query
        if to_date:
            options['to_date'] = getDateFormat( str(to_date) )
        if from_date:
            options['from_date'] = getDateFormat( str( from_date))
        if page_size:
            options['pagesize'] = page_size
        if has_images:
            options['has_images'] = has_images

        options['fields'] = ' '.join(ARTICLE_FIELDS)

        article_obj = NewscredApi('articles', options)
        results[article.block_choice] = article_obj.response()

    return results


ARTICLE_FIELDS_NEW = [
    'article.title',
    'article.guid',
    'article.description',
    'article.image.caption',
    'article.image.urls.large',
]





def render_article(request):
    #import pdb;pdb.set_trace()
    #guid = request.page_params['articleId'];
    #import pdb;pdb.set_trace();
    options={}
    guid=request.page_params['articleId']
    options['fields'] = ' '.join(ARTICLE_FIELDS_NEW)

    main_article_response = NewsCredApiArticle(guid,options).response()
    #print main_article_response.url
    #import pdb;pdb.set_trace()

    return main_article_response


def getDateFormat(dt):
    x = dt.split()
    return x[0]