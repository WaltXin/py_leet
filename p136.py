import unittest
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = num ^ result
        return result

class Test(unittest.TestCase):
    def test(self):
        self._test([1,2,1], 2)

    def _test(self, Li, expected):
        actual = Solution().singleNumber(Li)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
