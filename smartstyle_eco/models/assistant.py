from random import sample
from .outfit import Outfit
from .impact_report import ImpactReport

class StyleAssistant:
    def __init__(self, wardrobe):
        self.wardrobe = wardrobe

    def suggest_outfit(self):
        garments = self.wardrobe.get_garments()
        if len(garments) < 3:
            return None, None
        selected = sample(garments, 3)
        return Outfit(selected), ImpactReport(selected)
