
class Player:
    """
    Player class for a game.

    Attributes:
        name (str): Player's name.
        level (int): Current level of the player.
        health (int): Player's current health.
        max_health (int): Player's maximum possible health.
        inventory (list): Items collected by the player.
        attack (int): Attack power.
        defence (int): Defence power.
    """

    def __init__(self, name, level=1, max_health=100, attack=10, defence=5):
        self.name = name
        self.level = level
        self.max_health = max_health
        self.health = max_health
        self.inventory = []
        self.attack = attack
        self.defence = defence

    def take_damage(self, damage):
        """Reduces player health. Health won't go below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        """Heals the player. Health won’t go beyond max_health."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def add_item(self, item):
        """Adds an item to the player's inventory."""
        self.inventory.append(item)

    def __str__(self):
        return f"{self.name} (Lvl {self.level}) - HP: {self.health}/{self.max_health}, Inv: {self.inventory}"


class GameLevel:
    """
    Represents a game level or area.

    Attributes:
        name (str): Name of the level.
        items (list): Items available in this level.
    """

    def __init__(self, name, items=None):
        if items is None:
            items = []
        self.name = name
        self.items = items

    def give_items_to(self, player):
        """Moves all level items into player's inventory."""
        for item in self.items:
            player.add_item(item)
        self.items = []

    def __str__(self):
        return f"{self.name} Level - Items: {self.items}"


if __name__ == "__main__":
    player = Player("Leo")
    print(player)

    player.take_damage(25)
    player.heal(10)
    player.add_item("Axe")
    print(player)

    forest = GameLevel("Forest", ["Potion", "Map"])
    print(forest)
    forest.give_items_to(player)
    print(player)
