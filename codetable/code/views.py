import json
from random import randint

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from codetable.code.models import Code
from codetable.code.forms import CodeForm
from codetable.responselog.models import ResponseLog
from codetable.lib.utils import get_all_supported_languages
from codetable.hackerearth.settings import CLIENT_SECRET
from codetable.hackerearth.parameters import RunAPIParameters
from codetable.hackerearth.api_handlers import HackerEarthAPI


class CodeTableView(View):

    @staticmethod
    def get(request):
        """ Create new page for coding """
        code = Code()
        code.save()
        return HttpResponseRedirect('/code/%s' % code.id)

    @staticmethod
    def post(request, code_id=None):
        """ Save code when there is any change """
        try:
            code = get_object_or_404(Code, id=code_id)
            new_code = request.POST.get('code', '')
            lang = request.POST.get('lang', None)
            Code.objects.filter(id=code_id).update(code=new_code, language=lang)
            status = {'status': True}
        except Exception as e:
            status = {'status': False}
        return HttpResponse(json.dumps(status), content_type="application/json")


class CodeTableEditor(View):

    @staticmethod
    def get(request, code_id=None):
        template_name = 'html/codetable_editor.html'
        code = get_object_or_404(Code, id=code_id)
        data = {'text': code.code, 'inp': request.POST.get('inp',None)}
        form = CodeForm(data)
        return render(request, template_name, {'code': code.__dict__, 'languages': get_all_supported_languages(), 'form': form})

    @staticmethod
    def post(request, code_id=None):
        try:
            get_object_or_404(Code, id=code_id)
            source = request.POST.get('code', '')
            input_data = request.POST.get('input_data', '')
            lang = request.POST.get('lang', None)

            if input_data:
                params = RunAPIParameters(
                    client_secret=CLIENT_SECRET, program_input=input_data,
                    source=source, lang=lang, id=randint(0, 111111)
                )
            else:
                params = RunAPIParameters(
                    client_secret=CLIENT_SECRET,
                    source=source,
                    lang=lang,
                    id=randint(0, 111111)
                )

            api = HackerEarthAPI(params)
            api.compile()
            ret = api.run()

            if ret.status == "CE":
                ret.output_html = ""
                ret.memory_used = "0.0"
                ret.time_used = "0"

            response = ResponseLog(
                output_html=ret.output_html,
                run_status=ret.status,
                memory_used=ret.memory_used,
                time_used=ret.time_used,
                he_web_link=ret.web_link,
            )
            response.save()

            code = Code.objects.get(id=code_id)
            code.run_count += 1
            code.code = source
            code.language = lang
            code.input_stdin = input_data
            code.response = response
            code.save()

            ret.run_count = code.run_count
            ret.last_modified_date = response.created_at.strftime("%b. %d, %Y, %H:%M %p").replace(' 0', ' ')

            return HttpResponse(json.dumps(ret.__dict__), content_type="application/json")
        except Exception as err:
            return HttpResponse(json.dumps(err), content_type="application/json")
