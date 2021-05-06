import json

class Card:

    CARD_FILE = "cards.json"

    @staticmethod
    def load_cards():
        with open(Card.CARD_FILE) as f:
            return json.load(f)

    def __init__(self, data):
        self.card_type = data["cardType"]
        self.title = data["title"]
        self.text = data["text"]
        self.disabled = 0

    