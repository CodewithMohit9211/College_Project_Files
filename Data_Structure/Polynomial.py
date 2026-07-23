# Node Class
class Node:
    def __init__(self, coeff):
        self.coeff = coeff
        self.next = None

# Linked List Class
class Polynomial:
    def __init__(self):
        self.head = None

    # Insert coefficient
    def insert(self, coeff):
        new_node = Node(coeff)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Display Polynomial
    def display(self):
        temp = self.head
        power = 2
        while temp:
            print(f"{temp.coeff}x^{power}", end="")
            if temp.next:
                print(" + ", end="")
            temp = temp.next
            power -= 1
        print()

# Create Polynomials
p1 = Polynomial()
p2 = Polynomial()

print("Enter coefficients of Polynomial 1 (x², x, constant)")
for i in range(3):
    p1.insert(int(input()))

print("Enter coefficients of Polynomial 2 (x², x, constant)")
for i in range(3):
    p2.insert(int(input()))

print("\nPolynomial 1:")
p1.display()

print("Polynomial 2:")
p2.display()

# Addition
t1 = p1.head
t2 = p2.head

print("\nAddition:")
power = 2
while t1 and t2:
    print(f"{t1.coeff + t2.coeff}x^{power}", end="")
    if power > 0:
        print(" + ", end="")
    t1 = t1.next
    t2 = t2.next
    power -= 1

# Subtraction
t1 = p1.head
t2 = p2.head

print("\nSubtraction:")
power = 2
while t1 and t2:
    print(f"{t1.coeff - t2.coeff}x^{power}", end="")
    if power > 0:
        print(" + ", end="")
    t1 = t1.next
    t2 = t2.next
    power -= 1