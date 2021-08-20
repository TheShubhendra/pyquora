class Topic:
    """Class to represent a topic."""

    def __init__(self, json_data):
        self.id = json_data.get("id")
        self.name = json_data.get("name")
        self.url = "https://www.quora.com" + json_data.get("url")
        self.photoUrl = json_data.get("photoUrl")
        self.followerCount = json_data.get("numFollowers")
        self.userAnswersCount = json_data.get("numPublicAnswersOfUser")
        self.userAnswersUrl = "https://www.quora.com" + json_data.get("userAnswersUrl")

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["user"]
        return state

    def __setstate__(self, state):
        from .user import User

        self.__dict__.update(state)
        self.user = User(self.username)
