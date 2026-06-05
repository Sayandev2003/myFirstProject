#PATTERN 12

for row in range(1, 6):
    for col in range(row):
        print(row, end=" ")
    print()

#PATTERN 13
for row in range(5, 0, -1):
    for col in range(row):
        print(row, end=" ")
    print()

#PATTERN 14

for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

#PATTERN 16

for row in range (5):
    for col in range(1, 5 + 1):
        print(col, end=" ")
    print()

#PATTERN 15

for row in range(5):
    for col in range(0, row+1):
        print(chr(65+row), end=" ")
    print()

#PATTERN

for row in range(6):
    for col in range(row):
        print(chr(65+col), end=" ")
    print()

#PATTERN 17

for row in range(1, 6):
    for col in range(1, 6):
        
        if row == 1 or row == 5 or col == 1 or col == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#PATTERN 18 

for row in range(1, 6):

    for space in range(5 - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")
    print()

#PATTERN 19 PYRAMID

for row in  range(1, 6):
    
    for space in range(5 - row):
        print(" ", end=" ")
         
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()

#Pattern 20 multiplication table

for row in range(1, 11):
    for col in range(1, 11):
        print(row * col, end="\t")
    print()