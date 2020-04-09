import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_get_stock_price_summary1(self):
        """test stock_price_summary for list price_changes empty"""

        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(actual, expected)

    def test_get_stock_price_summary2(self):
        """test stock_price_summary for list price_changes with 0's"""

        actual = a1.stock_price_summary([0,0])
        expected = (0,0)
        self.assertEqual(actual, expected)

    def test_get_stock_price_summary3(self):
        """test stock_price_summary for list price_changes with negative values"""

        actual = a1.stock_price_summary([-0.02, -0.14, -0.10])
        expected = (0,-0.26)
        self.assertEqual(actual, expected)

    def test_get_stock_price_summary4(self):
        """test stock_price_summary for list price_changes with positive values"""

        actual = a1.stock_price_summary([0.02, 0.14, 0.10])
        expected = (0.26,0)
        self.assertEqual(actual, expected)

    def test_get_stock_price_summary5(self):
        """test stock_price_summary for list price_changes with positive and negative values"""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14,-0.17)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
