import json
import os

class Player:
    """
    Represents a game player with attributes like name, level, health,
    attack, defense, and inventory. Includes methods for taking damage,
    healing, collecting items, and saving/loading progress.

    Attributes:
        name (str): Name of the player.
        level (int): Player's current level.
        health (int): Current health.
        max_health (int): Maximum possible health.
        attack (int): Attack power.
        defense (int): Defense power.
        inventory (list): Items collected by the player.
    """

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.inventory = []

    def take_damage(self, amount):
        """Reduce player health based on damage taken."""
        self.health = max(self.health - amount, 0)
        print(f"{self.name} took {amount} damage. Health is now {self.health}/{self.max_health}")

    def heal(self, amount):
        """Increase health up to the max_health limit."""
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} healed for {amount}. Health is now {self.health}/{self.max_health}")

    def level_up(self):
        """Simulates player leveling up, improving stats."""
        self.level += 1
        self.max_health += 10
        self.attack += 3
        self.defense += 2
        self.health = self.max_health
        print(f"{self.name} is now Level {self.level}!")

    def pick_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"{self.name} picked up {item}")

    def show_info(self):
        """Displays current player status."""
        print("\n----- Player Info -----")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print("Items: ", self.inventory if self.inventory else "None")
        print("-----------------------\n")

    def save_to_json(self, filename):
        """Saves player data to a JSON file."""
        data = {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "max_health": self.max_health,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Game saved to {filename}")

    def load_from_json(self, filename):
        """Loads player data from a JSON file."""
        if not os.path.exists(filename):
            print("Save file not found.")
            return
        with open(filename, 'r') as f:
            data = json.load(f)
        self.name = data["name"]
        self.level = data["level"]
        self.health = data["health"]
        self.max_health = data["max_health"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.inventory = data["inventory"]
        print(f"Game loaded from {filename}")

# Example usage (this simulates gameplay)
if __name__ == "__main__":
    player = Player("Vinod")
    player.show_info()

    player.pick_item("VFX Sword")
    player.take_damage(10)
    player.heal(12)
    player.level_up()
    player.pick_item("Health Boost")
    player.show_info()

    # Save game state
    player.save_to_json("player_data.json")

    # Load to confirm
    print("\n--- Loading Player Again ---")
    new_player = Player("Temp")
    new_player.load_from_json("player_data.json")
    new_player.show_info()
