# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__ (self, current_room, items=[], health=6):
        self.current_room = current_room
        self.items = items
        self.health = int(health)

    def __str__(self):
        output = ""
        output += str(self.current_room) + "\n"
        if len(self.items) > 0:
            output += "Current items: "
            for i in self.items:
                output += "\n" + "\t" + str(i.name)
        output += "Current Health: " + str(self.health)
        return output
