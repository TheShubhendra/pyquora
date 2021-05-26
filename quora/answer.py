"""Answer class to represent a Quora answer."""
from quora.content import Content
from quora.question import Question


class Answer:
    def __init__(self, data_dict):
        self.id = data_dict.get("id")
        self.aid = data_dict.get("aid")
        self.isPinned = data_dict.get("isPinned")
        self.question = Question(data_dict.get("question"))
        self.url = "https://www.quora.com" + data_dict.get("permaUrl")
        self.content = Content(data_dict.get("content"))
        self.creationTime = data_dict.get("creationTime")
        self.updatedTime = data_dict.get("updatedTime")
        self.author = data_dict.get("author")

    def __str__(self):
        return self.content.__str__()

    def __eq__(self, other):
        return self.aid == other.aid
