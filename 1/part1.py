file = open("input.txt").readlines()

dial = 50
password = 0

for instruction in file:
    direction, distance = instruction[:1], int(instruction[1:])

    if direction == 'L':
        for _ in range(distance):
            dial = (dial - 1) % 100
    else:
        for _ in range(distance):
            dial = (dial + 1) % 100

    if dial == 0:
        password += 1

print(password)
