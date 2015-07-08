from django.shortcuts import render

from flicker.models import Flicker
from news.API import FlickerApi


def render(request, page=1):

    try:
        flckr = Flicker.objects.filter( page_id = page )[0]
    except IndexError:
        return False

    options = dict()

    text = flckr.text
    per_page = flckr.per_page

    if text:
        options['text'] = text
    if per_page:
        options['per_page'] = per_page

    return FlickerApi(options).response()