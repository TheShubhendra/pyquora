"""Contains Profile class."""
import json


class Profile:
    """Represent the profile of a quora user."""

    def __init__(self, user, data):
        """Constructor for Profile."""
        self.user = user
        self.username = user.username
        self.id = data.get("id")
        self.uid = data.get("uid")
        self.profileImage = data.get("profileImageUrl")
        try:
            self.firstName = data["names"][0]["givenName"]
        except Exception:
            self.firstName = None
        try:
            self.lastName = data["names"][0]["familyName"]
        except Exception:
            self.lastName = None
        try:
            self.profileCrendential = data["profileCredential"]["experience"]
        except Exception:
            self.profileCrendential = None
        try:
            text = ""
            description = json.loads(data.get("description"))
            for section in description["sections"]:
                for span in section["spans"]:
                    text += span["text"]
                text += "\n"
            self.profileBio = text
        except Exception:
            self.profileBio = "Not Available"
        self.contributingSpaceCount = data.get("numCanContributeTribes")
        self.twitterProfileUrl = data.get("twitterProfileUrl")
        self.answerViewsCount = data.get("allTimePublicAnswerViews")
        self.contentViewsCount = data.get("allTimePublicContentViews")
        self.lastMonthContentView = data.get("lastMonthPublicContentViews")
        self.answerCount = data.get("numPublicAnswers")
        self.questionCount = data.get("numProfileQuestions")
        self.shareCount = data.get("quoraSharesCount")
        self.postCount = data.get("numTribePosts", "N/A")
        self.followingCount = data.get("followingCount")
        self.followingSpaceCount = data.get("numFollowedTribes")
        self.followingTopicCount = data.get("numFollowedTopics")
        self.followerCount = data["followerCount"]

    def __str__(self):
        text = ""
        for i, j in vars(self).items():
            text += i + ": " + str(j) + "\n"
        return text

    def __eq__(self, other):
        return vars(self) == vars(other)

    def json(self):
        json = self.__dict__.copy().pop("user")
        return json

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["user"]
        return state

    def __setstate__(self, state):
        from .user import User

        self.__dict__.update(state)
        self.user = User(self.username)
