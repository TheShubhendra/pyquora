"""Data parsers for library."""
import json
import re

from quora.answer import Answer
from quora.topic import Topic
from .exceptions import ProfileNotFoundError

# noqa: E501
def parse_page(html_data, user):
    """Parse HTML and return JSON."""
    try:
        data = re.search(
            r'window\.ansFrontendGlobals\.data\.inlineQueryResults\.results\[".*\]\.push\((?P<extracted_data>\".*\")\);',
            html_data,
        )
        data = data.group('extracted_data')
        data = json.loads(json.loads(data))
        return data["data"]["user"]
    except Exception as e:
        # user.logger.warn("Unable to Parse the profile")
        raise ProfileNotFoundError(
            f"No profile\
found with the username {user.username}."
        )


def parse_answers(json_data, user, language):
    """Parse JSON string of answers and return list of `Answer` object."""
    answers = json_data["recentPublicAndPinnedAnswersConnection"]["edges"]
    return [Answer(ans["node"], user, language) for ans in answers]


def parse_topics(json_data, language):
    topics = json_data["expertiseTopicsConnection"]["edges"]
    return [Topic(topic["node"], language) for topic in topics]
