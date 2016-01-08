import json
import requests

from settings import COMPILE_API_ENDPOINT
from settings import RUN_TIME_UPPER_LIMIT
from settings import MEMORY_UPPER_LIMIT
from settings import RUN_API_ENDPOINT
from result import CompileResult
from result import RunResult


class HackerEarthAPI(object):
    def __init__(self, params):
        self.params_dict = params.get_params()

    def compile(self):
        response = self.__request(COMPILE_API_ENDPOINT, self.params_dict)
        result = CompileResult(response.text)
        if response.status_code != 200:
            result.valid = False
        else:
            result.valid = True
        return result

    def run(self):
        response = self.__request(RUN_API_ENDPOINT, self.params_dict)
        result = RunResult(response.text)
        if response.status_code !=200:
            result.valid = False
        else:
            result.valid = True
        return result

    def __request(self, url, params):
        response = None
        try:
            response = requests.post(url, data=params)
        except Exception, e:
            print e
        return response

    def __result(self, res):
        result = json.load(res)
        return result


class CustomHackerEarthAPIHandler(object):
    def __init__(self, client_secret, source, lang,
                 program_input=None,
                 time_limit=RUN_TIME_UPPER_LIMIT,
                 memory_limit=MEMORY_UPPER_LIMIT,
                 async=0,
                 id=None,
                 save=1,
                 memory_used=None,
                 callback='',
                 compressed=1,
                 html=1,
                 compiled=0):
        self.client_secret = client_secret
        self.source = source
        self.lang = lang
        self.program_input = program_input
        self.time_limit = time_limit,
        self.memory_limit = memory_limit,
        self.async = async,
        self.id = id,
        self.save = save,
        self.memory_used =memory_used
        self.callback = callback,
        self.compressed = compressed,
        self.html = html,
        self.compiled = compiled

    def run(self):
        data = {
            'client_secret': self.client_secret,
            'async': self.async,
            'source': self.source,
            'lang': self.lang,
            'input': self.program_input,
        }
        response = requests.post(RUN_API_ENDPOINT, data)
        return RunResult(response.content)
