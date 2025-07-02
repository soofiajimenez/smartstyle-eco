class ImpactReport:
    def __init__(self, garments):
        self.co2_kg = len(garments) * 2.5  # Simple estimation
        self.water_liters = len(garments) * 100

    def display(self):
        return f"Estimated CO2: {self.co2_kg}kg, Water: {self.water_liters}L"
