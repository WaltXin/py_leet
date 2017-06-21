import collections
import unittest


class Solution(object):
    def findLHS(self,nums):
        count = collections.Counter(nums)
        result = 0
        for x in count:
            if x + 1 in count:
                result = max(result,count[x] + count[x + 1])
        return result

class Test(unittest.TestCase):
    def test(self):
        self._test([1,1,1,2,3], 4)

    def _test(self, li, expected):
        actual = Solution().findLHS(li)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()