import json


class Content:
    def __init__(self, data_dict):
        if isinstance(data_dict, str):
            data_dict = json.loads(data_dict)
        self.data_dict = data_dict

    def parse(self, parse_mode="text"):
        text = ""
        if parse_mode == "text":
            for section in self.data_dict["sections"]:
                for span in section["spans"]:
                    text += span["text"]
                text += "\n"
        return text

    def __str__(self):
        return self.parse(parse_mode="text")
