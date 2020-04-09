import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_1(self):
        """Test for get_num_buses with n = 0. """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_2(self):
        """Test for get_num_buses with n = 49. """
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_3(self):
        """Test for get_num_buses with n = 50. """
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)


    def test_num_buses_4(self):
        """Test for get_num_buses with n = 51. """
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
