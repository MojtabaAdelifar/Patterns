

row = 4
column = 0
rows = 5
columns = 5

# outter loop for rows
for i in range(0, row):
    column += 1
    # inner loop for columns
    for j in range(0, column):
        print("*", end = ' ')
    print()

# outter loop iterates through the rows
for i in range(0, rows):
    columns -= 1
    # inner loop iterates through the columns
    for j in range(0, columns):
        print("*", end = ' ')
    print()


