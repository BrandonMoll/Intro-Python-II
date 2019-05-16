# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__ (self, current_room, items, health=6):
        self.current_room = current_room
        self.items = items
        self.health = int(health)

    def __repr__(self):
        return str(self.current_room)
