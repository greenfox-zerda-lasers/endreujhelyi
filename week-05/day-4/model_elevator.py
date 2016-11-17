# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remember that negative amount of people would be troubling

class Model:

    def __init__(self):
        self.num_floors = 12
        self.position = 0
        self.people = 0

    def add_people(self, add):
        self.people += add
        return self.people

    def remove_people(self, remove):
        self.people -= remove
        return self.people

    def elevator_pos(self, floor):
        self.position = floor
        return self.position