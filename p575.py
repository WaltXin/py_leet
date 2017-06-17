import unittest
class Solution(object):
    def distributeCandies(self, candies):
        sisterSet = set(candies)
        if len(sisterSet) >= len(candies) / 2:
            return len(candies) / 2
        else:
            return len(sisterSet)

class Test(unittest.TestCase):
    def test(self):
        self._test([1,1,1,1], 1)
        self._test([1,2,3,4,5,6],3)

    def _test(self, candie, expected):
        actual1 = Solution().distributeCandies(candie)
        self.assertEqual(actual1, expected)


if __name__ == '__main__':
    unittest.main()