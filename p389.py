import unittest

class Solution(object):
    def findTheDifference(self, s, t):
        ls = list(s)
        lt = list(t)
        for item in ls:
            if item in lt:
                lt.remove(item)
        return lt[0]

#ord convert char to int, chr convert int to char
class Solution2(object):
    def findTheDifference(self, s, t):
        ans = 0
        for item in s:
            ans ^= ord(item)
        for item in t:
            ans ^= ord(item)
        return chr(ans)

class Test(unittest.TestCase):
    def test(self):
        self._test('abbced','abbbced','b')

    def _test(self, ls, lt, expected):
        actual1 = Solution().findTheDifference(ls,lt)
        actual2 = Solution2().findTheDifference(ls, lt)
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)


if __name__ == '__main__':
    unittest.main()
