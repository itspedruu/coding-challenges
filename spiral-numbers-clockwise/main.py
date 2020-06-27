grids = 3

def get_clockwise_path(grid):
	base_point = (grid - 1, grid - 2)

	corner_steps = grid - 1
	steps = (2 * grid - 1) - 1

	corners = [(corner_steps, -corner_steps), (-corner_steps, -corner_steps), (-corner_steps, corner_steps), (corner_steps, corner_steps)]
	directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

	path = [base_point]

	for i in range(4):
		starting_point = base_point if i == 0 else corners[i - 1]
		direction = directions[i]

		for n in range(0, steps - 1 if starting_point == base_point else steps):
			path.append(tuple(map(sum, zip(path[-1], direction))))

	return path

def get_path():
	path = [(0, 0)]

	for grid in range(2, grids + 1):
		path += get_clockwise_path(grid)

	return path

def get_array_path():
	grid_path = get_path()

	center = [grids - 1, grids - 1]
	array_path = []

	for point in grid_path:
		index_point = list((map(sum, zip(center, point))))
		index_point.reverse()
		index_point[0] = 2 * grids - 2 - index_point[0]
		
		array_path.append(tuple(index_point))

	return array_path

def get_print_values():
	array_path = get_array_path()

	size = 2 * grids - 1
	values = [0] * size

	for i in range(size):
		values[i] = [0] * size
	
	current = 1

	for index_point in array_path:
		values[index_point[0]][index_point[1]] = str(current) if current >= 10 else ' ' + str(current)
		current += 1

	return values

print_values = get_print_values()

print('\n'.join([' '.join(value) for value in print_values]))