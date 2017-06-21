import unittest

import collections

class Solution(object):
    def leastBricks(self, wall):
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        return len(wall) - max(d.values())

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

class Test(unittest.TestCase):
    def test(self):
        self._test([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]], 2)

    def _test(self, li, expected):
        actual = Solution().leastBricks(li)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()