"""Question Class for quora question."""

from quora.content import Content


class Question:
    def __init__(self, data_dict):
        self.id = data_dict.get("id")
        self.qid = data_dict.get("qid")
        self.url = "https://www.quora.com" + data_dict.get("url")
        self.title = Content(data_dict.get("title"))

    def __str__(self):
        return self.title.__str__()

    def __eq__(self, other):
        return self.qid == other.qid
