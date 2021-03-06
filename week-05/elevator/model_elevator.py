
class Model:

    def __init__(self):
        self.num_floors = 12
        self.capacity = 9
        self.position = 0
        self.people = 0

    def add_people(self):
        if self.people < self.capacity:
            self.people += 1
        return self.people

    def remove_people(self):
        if self.people > 0:
            self.people -= 1
        return self.people

    def elevator_up(self):
        if self.position < self.num_floors:
            self.position += 1
        return self.position

    def elevator_down(self):
        if self.position > 0:
            self.position -= 1
        return self.position
