import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_1(self):
        """Test swap_k for k = 0"""

        L = [1, 2, 3, 4, 5, 6]
        k = 0
        actual = a1.swap_k(L, k)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_swap_k_2(self):
        """Test swap_k for k = 1"""

        L = [1, 2, 3, 4, 5, 6]
        k = 1
        actual = a1.swap_k(L, k)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_3(self):
        """Test swap_k for max k """

        L = [1, 2, 3, 4, 5, 6]
        k = int(len(L) / 2)
        actual = a1.swap_k(L, k)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_swap_k_4(self):
        """Test swap_k for max k and ood len L """

        L = [1, 2, 3, 4, 5]
        k = int(len(L) / 2)
        actual = a1.swap_k(L, k)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(actual, expected)

    def test_swap_k_5(self):
        """Test swap_k for max k and list of strings """

        L = ["uno", "dos", "tres", "cuatro"]
        k = int(len(L) / 2)
        actual = a1.swap_k(L, k)
        expected = ["tres", "cuatro","uno", "dos"]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
