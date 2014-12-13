from django import template
register = template.Library()
import json

@register.simple_tag
def cut(value, arg):
    return value.replace(arg, '')


@register.assignment_tag()
def resize_image(url, width, height):
    url =  url + '?width=%s&height=%s'
    return url % (width, height)

@register.assignment_tag()
def get_proper_image(image_list):
    image = None
    key = 0
    for img in image_list:
        if key==0:
            temp=img['width']
            image=img
        elif img.width>temp:
            image= img
            temp=img['width']
        # get largest
        #listCalc[counter]=img.width*img.height
    #max

    return image

@register.assignment_tag()
def getStr(strA , strB, size):
    s = strA + "  " + strB
    s = s[:size]
    return s