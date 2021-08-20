"""Answer class to represent a Quora answer."""
from quora.content import Content
from quora.question import Question


class Answer:
    def __init__(self, data_dict, user):
        """Constructs the `Answer` object."""
        self.id = data_dict.get("id")
        self.aid = data_dict.get("aid")
        self.isPinned = data_dict.get("isPinned")
        self.question = Question(data_dict.get("question"))
        self.url = "https://www.quora.com" + data_dict.get("permaUrl")
        self.content = Content(data_dict.get("content"))
        self.creationTime = data_dict.get("creationTime")
        self.updatedTime = data_dict.get("updatedTime")
        self.author = data_dict.get("author")
        self.user = user
        self.username = self.user.username

    def __str__(self):
        """Returns the answer text."""
        return self.content.__str__()

    def __eq__(self, other):
        """Returns whether two answers are same or not."""
        return self.aid == other.aid

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["user"]
        return state

    def __setstate__(self, state):
        from .user import User

        self.__dict__.update(state)
        self.user = User(self.username)
