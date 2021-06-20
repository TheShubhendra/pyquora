import json


class Content:
    """Represent the text content/
    inside of Question , Answer and other objects."""

    def __init__(self, data_dict):
        """Construts Content."""
        if isinstance(data_dict, str):
            data_dict = json.loads(data_dict)
        self.data_dict = data_dict

    def parse(self, parse_mode="text"):
        """Parses json into text."""
        text = ""
        if parse_mode == "text":
            for section in self.data_dict["sections"]:
                for span in section["spans"]:
                    text += span["text"]
                text += "\n"
        return text

    def __str__(self):
        """Returns the text representation."""
        return self.parse(parse_mode="text")
