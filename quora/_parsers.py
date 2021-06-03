import json
import re

from quora.answer import Answer
from .exceptions import ProfileNotFoundError


def parse_page(html_data):
    try:
        data = re.findall(
            r'window\.ansFrontendGlobals\.data\.inlineQueryResults\.results\[".*?"\] = ("{.*}");',
            html_data,
        )[-1]
        data = json.loads(json.loads(data))
    except Exception as e:
        raise ProfileNotFoundError("No profile found with this username."+str(e))
    return data["data"]["user"]


def parse_answers(json_data):
    answers = json_data["recentPublicAndPinnedAnswersConnection"]["edges"]
    return [Answer(ans["node"]) for ans in answers]
