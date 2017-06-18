import unittest


class Solution(object):
    def intersection(self, nums1, nums2):
        L = []
        for n1 in nums1:
            if n1 in nums2:
                if n1 not in L:
                    L.append(n1)
        return L

#using set quicker
class Solution2(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1&set2)

num1 = [1,2,3]
num2 = [3,3,3]

class Test(unittest.TestCase):
    def test(self):
        self._test(num1,num2,[3])

    def _test(self, ls, lt, expected):
        actual1 = Solution().intersection(ls,lt)
        actual2 = Solution2().intersection(ls, lt)
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)


if __name__ == '__main__':
    unittest.main()