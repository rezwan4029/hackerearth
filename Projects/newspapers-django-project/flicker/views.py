from django.shortcuts import render

from flicker.models import Flicker
from newspapers.API import FlickerApi
# Create your views here.

def render(request, page=1):

    try:
        flckr = Flicker.objects.filter( page_id = page )[0]
    except IndexError:
        return False

    options = {}

    text = flckr.text
    per_page = flckr.per_page

    if text:
        options['text'] = text
    if per_page:
        options['per_page'] = per_page

    Flicker_obj = FlickerApi(options)

    return Flicker_obj.response()