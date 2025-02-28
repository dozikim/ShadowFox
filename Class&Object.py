class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        """Display details of the Avenger."""
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.super_power}\n"
                f"Weapon: {self.weapon}\n"
                f"Leader: {'Yes' if self.is_leader() else 'No'}\n")

    def is_leader(self):
        """Check if the superhero is the leader."""
        return self.leader

# Creating Avengers
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", leader=True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 45, "Male", "Fighting Skills", "Bow and Arrows")
]

# Display information about each Avenger
for hero in super_heroes:
    print(hero.get_info())
    print("-" * 40)
