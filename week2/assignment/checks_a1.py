import a1

print(a1.num_buses(0))
print(a1.num_buses(49))
print(a1.num_buses(50))
print(a1.num_buses(51))

print(a1.stock_price_summary([]))
print(a1.stock_price_summary([0, 0]))
print(a1.stock_price_summary([ -0.02, -0.14, -0.10]))
print(a1.stock_price_summary([0.02, 0.14, 0.10]))
print(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]))

L = [1,2,3,4,5,6]
k = 0
print(a1.swap_k(L, k))


L = [1,2,3,4,5,6]
k = 1
print(a1.swap_k(L, k))


L = [1,2,3,4,5,6]
k = int(len(L)/2)
print(a1.swap_k(L, k))


L = [1,2,3,4,5]
k = int(len(L)/2)
print(a1.swap_k(L, k))

L = ["uno", "dos", "tres", "cuatro"]
k = int(len(L) / 2)

print(a1.swap_k(L, k))



k = int(len(L) / 2)


import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_example1(self):
        """ Test swap_k with list of even length and k = 2. """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        actual = nums
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected, actual)

    def test_swap_k_example2(self):
        """ Test swap_k with list of odd length and k = 1."""

        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 1)
        actual = nums
        expected = [5, 2, 3, 4, 1]
        self.assertEqual(expected, actual)

    def test_swap_k_example3(self):
        """ Test swap_k with list of int and k == len(L) // 2. """

        nums = [1, 2, 3, 4]
        a1.swap_k(nums, 2)
        actual = nums
        expected = [3, 4, 1, 2]
        self.assertEqual(expected, actual)

    def test_swap_k_example4(self):
        """ Test swap_k with list of str. """

        fruits = ['apple', 'banana', 'peach', 'orange']
        a1.swap_k(fruits, 2)
        actual = fruits
        expected = ['peach', 'orange', 'apple', 'banana']
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)

