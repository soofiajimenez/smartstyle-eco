class Outfit:
    def __init__(self, garments):
        self.garments = garments

    def __repr__(self):
        return ", ".join([str(g) for g in self.garments])
