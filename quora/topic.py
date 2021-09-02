class Topic:
    """Class to represent a topic."""

    def __init__(self, json_data):
        self.id = json_data.get("id")
        self.name = json_data.get("name")
        self.url = "https://www.quora.com" + json_data.get("url")
        self.photoUrl = json_data.get("photoUrl")
        self.followerCount = json_data.get("numFollowers")
        self.userAnswersCount = json_data.get("numPublicAnswersOfUser")
        # From August 2021 Quora started using dynamic loading of answers.
        #self.userAnswersUrl = "https://www.quora.com" + json_data.get("userAnswersUrl")

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id
