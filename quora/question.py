"""Question Class for quora question."""


class Question:
    def __init__(self, id, qid, url, title):
        self.id = (id,)
        self.qid = (qid,)
        self.url = url
        self.title = title
