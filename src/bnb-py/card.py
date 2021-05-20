import json

class Card:

    CARD_FILE = "cards.json"
    PROCEDURE = "Procedure"
    INITIAL = "Initial Compromise"
    INJECT = "Inject"
    PIVOT = "Pivot/Escalate"
    C2EXFIL = "C2/Exfil"
    PERSISTENCE = "Persistence"
    KILLCHAIN = [INITIAL, PIVOT, C2EXFIL, PERSISTENCE]

    @classmethod
    def create_card(cls, data):
        if data["cardType"] == cls.PROCEDURE:
            return Procedure(data)
        elif data["cardType"] == cls.INJECT:
            return Inject(data)
        else:
            return KillChain(data)

    @classmethod
    def load_cards(cls):
        with open(Card.CARD_FILE) as f:
            return [cls.create_card(j) for j in json.load(f)]
    
    @staticmethod
    def filter_cards(card_type, deck):
        return list(filter(lambda c: c.card_type == card_type, deck))

    def __init__(self, data):
        self.card_type = data["cardType"]
        self.title = data["title"]
        self.text = data["text"]
        self.disabled = 0

class Procedure(Card):
    def __init__(self, data):
        super().__init__(data)

class KillChain(Card):
    def __init__(self, data):
        super().__init__(data)
        self.detections = data["detections"]
        self.revealed = False

class Inject(Card):
    def __init__(self, data):
        super().__init__(data)