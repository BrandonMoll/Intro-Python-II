# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, attributes, items=[]):
        self.name = name
        self.attributes = attributes
        self.items = items

    def __str__(self):
        output = ""
        output += "Current Location: " + self.name + "\n" + "\n"
        output += "Description: " + self.attributes + "\n"
        if len(self.items) > 0:
            output += "Items in this room: "
            for i in self.items:
                output += "\n" + "\t" + str(i)
        return output