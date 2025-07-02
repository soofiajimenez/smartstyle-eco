class Wardrobe:
    def __init__(self):
        self.garments = []

    def add_garment(self, garment):
        self.garments.append(garment)

    def get_garments(self):
        return self.garments
