doors = [False] * 100

for step in range(1, 101):
    for i in range(step - 1, 100, step):
        doors[i] = not doors[i]

doors_state = [(doors[i], i + 1) for i in range(100)]

open_doors = []
closed_doors = []

for door_state in doors_state:
    if door_state[0] == True:
        open_doors.append(str(door_state[1]))
    else:
        closed_doors.append(str(door_state[1]))

print('Open Doors: {}\nDoors: {}\n\nClosed Doors: {}\nDoors: {}'.format(len(open_doors), ', '.join(open_doors), len(closed_doors), ', '.join(closed_doors)))