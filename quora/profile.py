import json


class Profile:
    def __init__(self, user, data):
        self.user = user
        self.username = user.username
        self.id = data["id"]
        self.uid = data["uid"]
        self.profileImage = data["profileImageUrl"]
        try:
            self.firstName = data["names"][0]["givenName"]
            self.lastName = data["names"][0]["familyName"]
        except:
            pass
        try:
            self.profileCrendential = data["profileCredential"]["experience"]
        except:
            pass
        try:
            text = ""
            description = json.loads(data["description"])
            for section in description["sections"]:
                for span in section["spans"]:
                    text += span["text"]
                text += "\n"
            self.profileBio = text
        except:
            self.profileBio = "Not Available"
        self.contributingSpaceCount = data["numCanContributeTribes"]
        self.twitterProfileUrl = data["twitterProfileUrl"]
        self.answerViewsCount = data["allTimePublicAnswerViews"]
        self.contentViewsCount = data["allTimePublicContentViews"]
        self.lastMonthContentView = data["lastMonthPublicContentViews"]
        self.answerCount = data["numPublicAnswers"]
        self.questionCount = data["numProfileQuestions"]
        self.shareCount = data["quoraSharesCount"]
        self.postCount = data["numTribePosts"]
        self.followingCount = data["followingCount"]
        self.followingSpaceCount = data["numFollowedTribes"]
        self.followingTopicCount = data["numFollowedTopics"]
        self.followerCount = data["followerCount"]

    def __str__(self):
        text = ""
        for i, j in vars(self).items():
            text += i + ": " + str(j) + "\n"
        return text

    def __eq__(self, other):
        return vars(self) == vars(other
        )
