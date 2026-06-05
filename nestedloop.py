for outer in range(3):
    for inner in range(2):
        print("Outer: ", outer, "Inner: ", inner)

 #example 2 square

for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()

#example 3 number square

for row in range(4):
    for col in range(4):
        print(row, end=" ")
    print()

#example 4 multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()

#example 5 square pattern

for row in range(5):
    for col in range(5):
        print("*", end="\t")
    print()

#example 6 right angle triangle

for i in range (1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#Example 7 number triangle

for row in range(1, 6):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

#example 8 trianle pattern

for i in range(1, 6):
    for j in range(i):
        print("A", end=" ")
    print()

#example 9 triangle pattern

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

#example 10 triangle pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#example 11 

for row in range(5, 0, -1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()