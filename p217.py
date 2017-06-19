import unittest


#straightforward logic
class Solution(object):
    def containsDuplicate(self, nums):
        i = 0
        for item in nums:
            i = i + 1
            if item in nums[i:]:
                return True
                break
        return False

#Always using set attribution
class Solution2(object):
    def containsDuplicate(self, nums):
        sets = set(nums)
        if len(sets) == len(nums):
            return False
        else:
            return True


class Test(unittest.TestCase):
    def test(self):
        self._test([1,2,3], False)
        self._test([1,2,2,1], True)
        self._test([0],False)
        self._test([3,3], True)
    def _test(self, Li, expected):
        actual = Solution().containsDuplicate(Li)
        self.assertEqual(actual, expected)

        actual1 = Solution2().containsDuplicate(Li)
        self.assertEqual(actual1, expected)


if __name__ == '__main__':
    unittest.main()