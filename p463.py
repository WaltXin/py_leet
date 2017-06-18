import unittest

class Solution(object):
    def islandPerimeter(self, grid):
        island = 0
        neighbors = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island = island + 1
                    #calculate how many right neighbors and down neighbors
                    if i + 1< len(grid) and grid[i + 1][j] == 1:
                        #down neighbors
                        neighbors = neighbors + 1
                    if j + 1< len(grid[i]) and grid[i][j + 1] == 1:
                        #right neighbors
                        neighbors = neighbors + 1
        return island * 4 - neighbors * 2



grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

class Test(unittest.TestCase):
    def test(self):
        self._test(grid, 16)

    def _test(self, brige, expected):
        actual = Solution().islandPerimeter(brige)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()