import unittest

class Solution:
    def multiples_of_3_and_5(self,num):
        sum = 0
        for i in range(num):
            if (i % 3 == 0) or (i % 5 == 0):
                sum += i
        return sum


# 233168
class SolutionTest(unittest.TestCase):
    def test_multiples_of_3_and_5(self):
        num = 1000

        self.assertEqual(Solution().multiples_of_3_and_5(num), 233168)

    def test_multiples_of_3_and_5_zero_num(self):
        num1 = 0

        self.assertEqual(Solution().multiples_of_3_and_5(num1), 0)

    def test_multiples_of_3_and_5_zero_num_big_input(self):
        num = 1000000000

        self.assertEqual(Solution().multiples_of_3_and_5(num), 233333333166666668)

if __name__ == '__main__':
    unittest.main()