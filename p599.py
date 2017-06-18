import unittest

import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        result = []
        index = len(list1) + len(list2)
        for l1 in range(len(list1)):
            for l2 in range(len(list2)):
                if list1[l1] == list2[l2]:
                    if l1 + l2 <= index:
                        index = l1 + l2
                        result.append(list1[l1])
        return result

class Solution2(object):
    def findRestaurant(self, list1, list2):
        D1 = dict(zip(list1,range(len(list1))))
        D2 = dict(zip(list2,range(len(list2))))
        result = {}
        for key in D1.keys():
            if key in D2.keys():
                index = D1.get(key) + D2.get(key)
                result.update({key:index})

        output =[]
        minValue = len(list1) + len(list2)
        for key in result.keys():
            if result.get(key) <= minValue:
                minValue = result.get(key)
        for key in result.keys():
            if result.get(key) == minValue:
                output.append(key)

        return output








L1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
L2 = ["KFC", "Shogun", "Burger King"]

L3 = ["Shogun","Tapioca Express","Burger King","KFC"]
L4 = ["KFC","Burger King","Tapioca Express","Shogun"]
class Test(unittest.TestCase):
    def test(self):
        self._test(L1,L2,["Shogun"])
        self._test(L3,L4,['Shogun', 'Tapioca Express', 'Burger King', 'KFC'])

    def _test(self, str1, str2, expected):
        actual1 = Solution().findRestaurant(str1,str2)
        self.assertEqual(actual1,expected)
        actual2 = Solution().findRestaurant(str1, str2)
        self.assertEqual(actual2, expected)
        actual3 = Solution2().findRestaurant(str1, str2)
        self.assertEqual(actual3, expected)
        actual4 = Solution2().findRestaurant(str1, str2)
        self.assertEqual(actual4, expected)


