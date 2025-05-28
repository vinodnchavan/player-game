# Player Game Project

## Overview
This project implements a simple Python class called `Player` that represents a player in a game. The class captures basic attributes like the player's name, level, health, inventory, attack power, and defense power. It also includes behaviors such as taking damage, healing, and collecting items.

Additionally, an optional `GameLevel` class is provided to represent different game levels with items that the player can collect.

## Features
- Player attributes: name, level, health, max health, inventory, attack, and defense.
- Player methods to:
  - Take damage without health dropping below zero.
  - Heal without exceeding maximum health.
  - Collect items into an inventory.
- GameLevel class to simulate game environments with collectible items.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the folder containing `player_game.py`.
4. Run the script using:
   ```bash
   python player_game.py
