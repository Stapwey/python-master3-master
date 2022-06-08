class SomeClass:

    def __init__(self):
        self.state = "A"

    def daub(self):
        if (self.state == "A"):
            self.state = "B"
            return 0
        elif (self.state == "D"):
            self.state = "D"
            return 5
        elif (self.state == "E"):
            self.state = "E"
            return 7
        else:
            raise KeyError(self.state)

    def march(self):
        if (self.state == "B"):
            self.state = "C"
            return 1
        elif (self.state == "C"):
            self.state = "D"
            return 2
        elif (self.state == "D"):
            self.state = "E"
            return 3
        elif (self.state == "E"):
            self.state = "F"
            return 6
        elif (self.state == "F"):
            self.state = "C"
            return 8
        else:
            raise KeyError(self.state)

    def chip(self):
        if (self.state == "D"):
            self.state = "F"
            return 4
        else:
            raise KeyError(self.state)


def main():
    return SomeClass()
