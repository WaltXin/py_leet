import unittest


class Solution(object):
    def leastBricks(self, wall):
        for i in range(len(wall)):
            for j in range(len(wall[i])):
                if j != 0:
                    wall[i][j] = wall[i][j] + wall[i][j - 1]
        maxCount = 0
        for i in range(len(wall)):
            for j in range(len(wall[i]) - 1):
                count = 0
                for m in range(i, len(wall)):
                    for n in range(len(wall[m]) - 1):
                        if wall[i][j] == wall[m][n]:
                            count = count + 1
                if count > maxCount:
                    maxCount = count
        return len(wall) - maxCount


L = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
class Test(unittest.TestCase):
    def test(self):
        self._test(L, 2)

    def _test(self, li, expected):
        actual = Solution().leastBricks(li)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()