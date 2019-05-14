# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __repr__(self):
        output = ""
        output += "Current Location: " + self.name + "\n"
        output += self.attributes
        return output