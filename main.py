from smartstyle_eco.models.user import User
from smartstyle_eco.models.garment import Garment
from smartstyle_eco.models.wardrobe import Wardrobe
from smartstyle_eco.models.assistant import StyleAssistant

# Create user and wardrobe
user = User(user_id=1, name="Sofía", preferences={"style": "casual"})
wardrobe = Wardrobe()

# Add garments
wardrobe.add_garment(Garment("Blue Shirt", "blue", "spring", "new"))
wardrobe.add_garment(Garment("Jeans", "denim", "all", "new"))
wardrobe.add_garment(Garment("Sneakers", "white", "all", "second-hand"))
wardrobe.add_garment(Garment("Jacket", "black", "winter", "new"))

# Generate outfit and report
assistant = StyleAssistant(wardrobe)
outfit, report = assistant.suggest_outfit()

if outfit:
    print(f"Suggested outfit: {outfit}")
    print(report.display())
else:
    print("Not enough garments to suggest an outfit.")
