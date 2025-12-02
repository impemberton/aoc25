

class Safe:
    def __init__(self):
        self.pointer = 50
        self.zero_count = 0

    def rotate(self, rotation):
        amount = int(rotation[1:])
        if rotation[0] == "L":
            self.rotate_left(amount)
        else:
            self.rotate_right(amount)

        if self.pointer == 0:
            self.zero_count += 1
    
    def rotate_left(self, amount):
        self.pointer -= amount % 100
        if self.pointer < 0:
            self.pointer += 100

    def rotate_right(self, amount):
        self.pointer += amount % 100
        if self.pointer > 99:
            self.pointer -= 100


def main():
    safe = Safe()
    with open("input.txt") as input:
        for rotation in input:
            safe.rotate(rotation)

    print(safe.zero_count)
    
main()
