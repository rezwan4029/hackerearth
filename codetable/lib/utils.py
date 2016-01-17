import random
import string

from codetable.hackerearth.parameters import SupportedLanguages


def id_generator(max_size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(max_size))


def get_all_supported_languages(lang=None):
    languages = []
    for key, value in SupportedLanguages.__dict__.iteritems():
        if isinstance(value, basestring):
            if not value.startswith('__') and value == key:
                print lang, " : ", value
                if lang and lang != value:
                    languages.append(value)
    languages = sorted(languages, reverse=False)

    if lang:
        ans = [lang]
        ans.extend(languages)
        return ans

    return languages