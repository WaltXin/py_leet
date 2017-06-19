import unittest


class Solution(object):
    def isHappy(self, n):
        li_repeat = []
        li_repeat.append(n)

        li = list(str(n))
        while n != 1:
            n = 0
            for value in li:
                n += int(value) * int(value)
            li = list(str(n))
            if n not in li_repeat:
                li_repeat.append(n)
            elif n in li_repeat:
                return False
        return True

class Test(unittest.TestCase):
    def test(self):
        self._test(19,True)
        self._test(20,False)

    def _test(self, ls,expected):
        actual = Solution().isHappy(ls)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()