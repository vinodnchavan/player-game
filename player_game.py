
"""
    A class to represent a player in a game.

    Attributes:
        name (str): The player's name.
        level (int): The current level of the player.
        health (int): The player's current health.
        max_health (int): The max health player can have at current level.
        attack (int): Attack power of the player.
        defense (int): Defensive strength of the player.
        inventory (list): A list of items the player collects.
    """

class Player:
  

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.inventory = []  # Holds items player picks up during gameplay

        """
        Calculates effective damage after defense is applied.
        Health can't drop below 0.
        """

    def take_damage(self, damage):  
       
        actual_damage = max(0, damage - self.defense)
        self.health = max(0, self.health - actual_damage)
        print(f"{self.name} took {actual_damage} damage. Health is now {self.health}/{self.max_health}")
    """
        Restores health up to max_health.
        """
    def heal(self, amount):
        
        if self.health == self.max_health:
            print(f"{self.name} is already at full health.")
        else:
            self.health = min(self.max_health, self.health + amount)
            print(f"{self.name} healed for {amount}. Health is now {self.health}/{self.max_health}")

    """
        Adds a collected item to inventory.
        """
    def pick_item(self, item):
        
        self.inventory.append(item)
        print(f"{self.name} picked up {item}")
    """
        Increases player's stats and restores health.
        Called when player gains enough experience (not tracked here).
        """
    def level_up(self):
        
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack += 3
        self.defense += 2
        print(f"{self.name} is now Level {self.level}!")
    """
        Prints the player's current state.
        """
    def show_status(self):
        
        print("\n----- Player Info -----")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Items: {self.inventory if self.inventory else 'None'}")
        print("-----------------------\n")


# Simulating a gameplay scenario to show output

if __name__ == "__main__":
    # Creating a player instance
    player1 = Player("Vinod")

    # Show initial status
    player1.show_status()

    # Pick up a weapon item
    player1.pick_item("VFX Sword")

    # Take some damage during gameplay
    player1.take_damage(15)

    # Heal some HP
    player1.heal(10)

    # Level up (e.g., after completing a quest)
    player1.level_up()

    # Pick another item
    player1.pick_item("Health Boost")

    # Final status after multiple actions
    player1.show_status()

