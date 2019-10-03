# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """docstring for Player."""

    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name

    def getCurrentRoom(self):
        return self.current_room

    def getName(self):
        return self.name

    def setRoom(self, current_room):
        self.current_room = current_room
