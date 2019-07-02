from math import sqrt

class Solution:
    def validateGrid(self, grid):
        def check(coords):
            [minCoord, maxCoord] = coords
            return 0 <= minCoord < 10 ** 6 and 0 <= maxCoord < 10 ** 6 if len(coords) == 2 else False
        
        validations = [True for coords in grid if check(coords)]
        return len(validations) == len(grid)
    
    def validateBlocked(self, blocked):
        validations = [True for element in blocked if len(element) == 2]
        return len(validations) == len(blocked) and 0 <= len(blocked) <= 200

    def nearestCellsToWalk(self, location, path, ignoredCells):
        nearestCells = [[location[0] + 1, location[1]], [location[0], location[1] + 1], [location[0] - 1, location[1]], [location[0], location[1] - 1]]
        return [cell for cell in nearestCells if cell not in ignoredCells and cell not in path and self.validateGrid([cell])]

    def nearestCellToTarget(self, target, nearestCells):
        nearestCell = nearestCells[0]

        for cell in nearestCells:
            distanceFromCurrentNearestCell = sqrt((target[0] - nearestCell[0]) ** 2 + (target[1] - nearestCell[1]) ** 2)
            distanceFromCell = sqrt((target[0] - cell[0]) ** 2 + (target[1] - cell[1]) ** 2)

            if distanceFromCell < distanceFromCurrentNearestCell:
                nearestCell = cell

        return nearestCell

    def getAccessibleCellsInRadius(self, radius, cell):
        def getCellsInRadius(i):
            if i % 2 == 0:
                return [cell[0] + (radius if i == 0 else -radius), cell[1]]
            else:
                return [cell[0], cell[1] + (radius if i == 1 else -radius)]

        cellsInRadius = [getCellsInRadius(i) for i in range(4)]
        accessibleCells = [cellInRadius for cellInRadius in cellsInRadius if self.validateGrid([cellInRadius])]

        if len(accessibleCells) == 0:
            self.getAccessibleCellsInRadius(radius + 1, cell)
        else:
            return accessibleCells
    
    def attemptEscape(self, source, target):
        location = source
        path = []
        ignoredCells = self.blocked

        while location != target:
            nearestCells = self.nearestCellsToWalk(location, path, ignoredCells)

            if len(nearestCells) == 0 and location == source:
                return False
            elif len(nearestCells) == 0:
                ignoredCells.append(location)
                location = source
            else:
                location = self.nearestCellToTarget(target, nearestCells)
                path.append(location)

        return True
        
    def isEscapePossible(self, blocked, source, target):
        self.grid = [[0,999999], [0, 999999]]
        self.blocked = blocked
        
        if len(source) < 2 or len(target) < 2:
            return False
        elif not self.validateBlocked(blocked):
            return False
        elif not self.validateGrid(self.grid) or not self.validateGrid([source, target]) or not self.validateGrid(blocked):
            return False
        elif source == target:
            return False
        
        if len(blocked) == 0:
            return True

        distanceFromSourceToTarget = sqrt((source[0] - target[0]) ** 2 + (source[1] - target[1]) ** 2)

        if distanceFromSourceToTarget > 200:
            cellsToEscapeSource = self.getAccessibleCellsInRadius(200, source)
            cellsToEscapeTarget = self.getAccessibleCellsInRadius(200, target)

            escapeSource = len([1 for cell in cellsToEscapeSource if self.attemptEscape(source, cell)]) > 0
            escapeTarget = len([1 for cell in cellsToEscapeTarget if self.attemptEscape(target, cell)]) > 0
            return escapeSource and escapeTarget
        else:
            return self.attemptEscape(source, target)

escape = Solution().isEscapePossible([[100005,100073],[100006,100074],[100007,100075],[100008,100076],[100009,100077],[100010,100078],[100011,100079],[100012,100080],[100013,100081],[100014,100082],[100015,100083],[100016,100084],[100017,100085],[100018,100086],[100019,100087],[100020,100088],[100021,100089],[100022,100090],[100023,100091],[100024,100092],[100025,100091],[100026,100090],[100027,100089],[100028,100088],[100029,100087],[100030,100086],[100031,100085],[100032,100084],[100033,100083],[100034,100082],[100035,100081],[100036,100080],[100037,100079],[100038,100078],[100039,100077],[100040,100076],[100041,100075],[100042,100074],[100043,100073],[100044,100072],[100043,100071],[100042,100070],[100041,100069],[100040,100068],[100039,100067],[100038,100066],[100037,100065],[100036,100064],[100035,100063],[100034,100062],[100033,100061],[100032,100060],[100031,100059],[100030,100058],[100029,100057],[100028,100056],[100027,100055],[100026,100054],[100025,100053],[100024,100052],[100023,100053],[100022,100054],[100021,100055],[100020,100056],[100019,100057],[100018,100058],[100017,100059],[100016,100060],[100015,100061],[100014,100062],[100013,100063],[100012,100064],[100011,100065],[100010,100066],[100009,100067],[100008,100068],[100007,100069],[100006,100070],[100005,100071]], [100024,100072],[999994,999990])
print('{} possible to escape the maze'.format('It\'s' if escape == True else 'It\'s not'))