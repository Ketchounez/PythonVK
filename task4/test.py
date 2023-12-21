from metaclass import CustomClass
import discriptor
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()
        self.magazine = discriptor.Magazine
        self.magazine.street = "Dubosekovskay"
        self.magazine.number_of_house = 5
        self.magazine.amount_of_products = 10**4



    def test_metaclass_1(self):
        self.assertEqual(CustomClass.custom_x, 50)

    def test_metaclass_2(self):

        with self.assertRaises(AttributeError):
            self.assertFalse(CustomClass.x)

    def test_metaclass_3(self):
        self.assertEqual(self.inst.custom_x, 50)

    def test_metaclass_4(self):
        self.assertEqual(self.inst.custom_val, 99)

    def test_metaclass_5(self):
        self.assertEqual(self.inst.custom_line(), 100)

    def test_metaclass_6(self):
        self.assertEqual(str(self.inst), "Custom_by_metaclass")

    def test_metaclass_7(self):
        with self.assertRaises(AttributeError):
            self.assertFalse(self.inst.x)

    def test_metaclass_8(self):
        with self.assertRaises(AttributeError):
            self.assertFalse(self.inst.val)

    def test_metaclass_9(self):
        with self.assertRaises(AttributeError):
            self.assertFalse(self.inst.line())

    def test_metaclass_10(self):
        with self.assertRaises(AttributeError):
            self.assertFalse(self.inst.yyy)

    def test_discriptor(self):
        self.assertTrue(self.magazine.street, "Dubosekovskay")
        self.assertNotEqual(self.magazine.number_of_house, 50)

        discriptor.Magazine.number_of_house = 50
        self.assertEqual(self.magazine.number_of_house, 50)

        self.magazine2 = discriptor.Magazine
        self.magazine2.street = "Mira"
        self.magazine2.amount_of_products = 10 ** 3

        self.assertEqual(self.magazine2.number_of_house, 50)


if __name__ == "__main__":
    unittest.main()