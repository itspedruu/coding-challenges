class Solution:
	def findSolution(self, customFunction, z):
		x = 0
		y = 0
		pairs = []

		for i in range(1, 1001):
			x += 1
			
			for n in range(1, 1001):
				y += 1

				if customFunction(x, y) == z:
					pairs += [[x, y]]
				elif customFunction(x, y) > z:
					break

			y = 0

		return pairs

custom_function = lambda x, y: x * y
solution = Solution().findSolution(custom_function, 5)

print('Solutions: {}'.format(solution))