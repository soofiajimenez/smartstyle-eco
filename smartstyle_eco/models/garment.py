class Garment:
    def __init__(self, name, color, season, condition):
        self.name = name
        self.color = color
        self.season = season
        self.condition = condition  # new or second-hand

    def __repr__(self):
        return f"{self.name} ({self.color}, {self.season}, {self.condition})"
