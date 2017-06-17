import unittest

#check first char in which row and the rest char in same row or not
class Solution(object):
    def findWords(self,words):
        L = []
        for word in words:
            l_word = list(word)
            firstChar = l_word[0]
            firstCharRow = self.match(firstChar)
            passed = 'true'
            for restChar in l_word[1:]:
                if firstCharRow != self.match(restChar):
                    passed = 'false'
                    break
            if passed == 'true':
                L.append(word)
        return L

    def match(self,char):
        L1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        L2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        L3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        if char.lower() in L1:
            return "L1"
        elif char.lower() in L2:
            return "L2"
        elif char.lower() in L3:
            return "L3"

#Second solution(using set)
class Solution2(object):
    def findWords(self,words):
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        result = []
        for word in words:
            t = set(word.lower())
            if t & a == t:
                result.append(word)
            if t & b == t:
                result.append(word)
            if t & c == t:
                result.append(word)
        return result

class Test(unittest.TestCase):
    def test(self):
        self._test(['adfsd','fefe'], ['adfsd'])
        self._test(['qaz','wws'],[])

    def _test(self, words, expected):
        actual1 = Solution().findWords(words)
        actual2 = Solution2().findWords(words)
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)


if __name__ == '__main__':
    unittest.main()