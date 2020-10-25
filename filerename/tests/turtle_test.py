import unittest
import filerename.dynamic.turtle as turtle


class TestTurtleRouting(unittest.TestCase):

    def test_upper(self):
        a = [
            [9, 8, 6, 2],
            [10, 11, 13, 11],
            [3, 7, 12, 8],
            [5, 9, 13, 9],
        ]
        max_way = turtle.solve(a)
        print("Max way is: {}".format(max_way))
        self.assertEqual(max_way, 65)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
