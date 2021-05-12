import json

class Card:

    CARD_FILE = "cards.json"
    PROCEDURE = "Procedure"
    INJECT = "Inject"
    PIVOT = "Pivot/Escalate"
    C2EXFIL = "C2/Exfil"
    PERSISTENCE = "Persistence"

    @staticmethod
    def load_cards():
        with open(Card.CARD_FILE) as f:
            return [Card(j) for j in json.load(f)]

    def __init__(self, data):
        self.card_type = data["cardType"]
        self.title = data["title"]
        self.text = data["text"]
        self.disabled = 0

class Procedure(Card):

    def __init__(self, data):
        super(data)
        