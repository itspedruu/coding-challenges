from math import sqrt

class Solution:
    def numberOfBoomerangs(self, points):
        if len(points) < 3:
            return 0

        boomerangs = 0

        for i in points:
            distances = {}

            for j in points:
                if j != i:
                    distance = sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
                    
                    if distance in distances:
                        distances[distance].append(j)
                    else:
                        distances[distance] = [j]

            if len(distances) > 0:
                boomerangs += sum([len(distance) * (len(distance) - 1) for distance in distances.values() if len(distance) > 1])

        return boomerangs

boomerangs = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
print('Number of Boomerangs: {}'.format(boomerangs))