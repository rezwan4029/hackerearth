from django.http import Http404
from pages.views import render
from pages.models import Page


class PagesMiddleWare(object):

    def process_request(self, request):
        #test_string="this is only gor teting purpose";#request.get_full_path();
        current_path = request.path
        if (not current_path.startswith('/static') and not current_path.startswith('/admin') and not current_path.startswith('/api') and
            not current_path.startswith('/login') and not current_path.startswith('/logout')):

            page, params = Page.get_current_page(current_path)

            if not page:
                raise Http404

            setattr(request, 'page', page)
            setattr(request, 'page_params', params)