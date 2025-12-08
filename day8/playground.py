import math

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = Circuit(self)

    def get_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        
        return JunctionBoxDistance(self, other, math.sqrt(dx**2 + dy**2 + dz**2))

    def connect(self, other):
        self.circuit.merge(other.circuit)

    def __eq__(self, other):
        x_same = self.x == other.x
        y_same = self.y == other.y
        z_same = self.z == other.z
        return x_same and y_same and z_same

    def __str__(self):
        return f"JunctionBox(x: {self.x}, y: {self.y}, z: {self.z})"

    def repr(self):
        return f"JunctionBox(x: {self.x}, y: {self.y}, z: {self.z})"

class JunctionBoxDistance:
    def __init__(self, junction_box1, junction_box2, distance):
        self.junction_box1 = junction_box1
        self.junction_box2 = junction_box2
        self.distance = distance

    def __str__(self):
        return f"Distance between {self.junction_box1} and {self.junction_box2}: {self.distance}"

class Circuit:
    def __init__(self, initial_junction_box) -> None:
        self.junction_boxes = [initial_junction_box]

    def get_size(self):
        return len(self.junction_boxes)
    
    def merge(self, other):
        if self != other:
            for junction_box in other.junction_boxes:
                self.junction_boxes.append(junction_box)
                junction_box.circuit = self
            other.junction_boxes = []
        


def main():
    junction_boxes = []
    with open("input.txt") as input:
        for line in input:
            x, y, z = line.split(",")
            junction_boxes.append(JunctionBox(int(x),int(y),int(z)))

    distances = []
    for i, junction_box1 in enumerate(junction_boxes):
        for junction_box2 in junction_boxes[i+1:]:
            distances.append(junction_box1.get_distance(junction_box2))

    sorted_distances = sorted(distances, key=lambda d: d.distance )
    
    pairs_to_connect = 1000

    circuits = [] 
    for i in range(pairs_to_connect):
        sorted_distances[i].junction_box1.connect(sorted_distances[i].junction_box2)
        circuits.append(sorted_distances[i].junction_box1.circuit)

    top_three_circuits = [circuit.get_size() for circuit in sorted(set(circuits),key=lambda circuit: circuit.get_size(), reverse=True)][:3]
    print(top_three_circuits)
    prod_of_top_three = 1
    for size in top_three_circuits:
        prod_of_top_three *= size
    print(prod_of_top_three)

main()
