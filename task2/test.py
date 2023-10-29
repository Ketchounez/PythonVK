"""Module for test"""
import unittest
from main import CustomList


class Test(unittest.TestCase):
    """Test class for CustomList"""

    def test_list_plus_customlist(self):
        """Test when the list is on the left"""
        self.assertEqual([1, 2, 3] + CustomList([1, 2, 3, 4]), CustomList([2, 4, 6, 4]))

    def test_customlist_plus_list(self):
        """Test when the CustomList is on the left"""
        self.assertEqual(CustomList([9, 9, 9, 9]) + [1, 2, 3], CustomList([10, 11, 12, 9]))

    def test_list_minus_customlist(self):
        """Test when the list is on the left"""
        self.assertEqual([1, 2, 3] - CustomList([1, 2, 3, 4]), CustomList([0, 0, 0, -4]))

    def test_customlist_minus_list(self):
        """Test when the CustomList is on the left"""
        self.assertEqual(CustomList([1, 2, 7, 8, 9]) - [0, 0, 2, 1], CustomList([1, 2, 5, 7, 9]))

    def test_eq_true(self):
        """Test eq"""
        self.assertTrue(CustomList([2, 1, 6]) == CustomList([9]))

    def test_eq_false(self):
        """Test eq"""
        self.assertFalse(CustomList([7, 7, 2, 9]) == CustomList([2, 4, 20]))

    def test_ne_true(self):
        """Test ne"""
        self.assertTrue(CustomList([2, 1, 1]) != CustomList([9, 3, 3]))

    def test_ne_false(self):
        """Test ne"""
        self.assertFalse(CustomList([1, 9, 3]) != CustomList([2, 3, 8]))

    def test_gt_true(self):
        """Test gt"""
        self.assertTrue(CustomList([4]) > CustomList([1, 2, 0]))

    def test_gt_false(self):
        """Test gt"""
        self.assertFalse(CustomList([6]) > CustomList([3, 7]))

    def test_ge_true(self):
        """Test ge"""
        self.assertTrue(CustomList([4]) >= CustomList([2, 2]))

    def test_ge_false(self):
        """Test ge"""
        self.assertFalse(CustomList([4]) >= CustomList([1, 3, 1]))


if __name__ == "__main__":
    unittest.main()
