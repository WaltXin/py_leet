import unittest


class Solution(object):
    def longestPalindrome(self, s):
        li = list(s)
        li_int = [0] * 256
        for item in li:
            li_int[ord(item)] = li_int[ord(item)] + 1
        count = 0
        for item in li_int:
            if item % 2 != 0:
                count = count + 1
        if count == 0:
            count = 1
        return len(s) - count + 1

class Test(unittest.TestCase):
    def test(self):
        self._test('AaBbfjosejif',5)

    def _test(self, ls,expected):
        actual = Solution().longestPalindrome(ls)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
