"""Data parsers for library."""
import json
import re

from quora.answer import Answer
from quora.topic import Topic
from .exceptions import ProfileNotFoundError


def parse_page(html_data, user):
    """Parse HTML and return JSON."""
    try:
        data = re.findall(
            r'window\.ansFrontendGlobals\.data\.inlineQueryResults\.results\[".*?"\] = ("{.*}");',  # noqa: E501
            html_data,
        )[-1]
        data = json.loads(json.loads(data))
        return data["data"]["user"]
    except Exception as e:
        user.logger.exception("Unable to Parse the profile")
        raise ProfileNotFoundError(
            f"No profile\
found with the username {user.username}."
        )


def parse_answers(json_data, user):
    """Parse JSON string of answers and return list of `Answer` object."""
    answers = json_data["recentPublicAndPinnedAnswersConnection"]["edges"]
    return [Answer(ans["node"], user) for ans in answers]


def parse_topics(json_data):
    topics = json_data["expertiseTopicsConnection"]["edges"]
    return [Topic(topic["node"]) for topic in topics]
