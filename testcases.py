import unittest
import exer

class MyTest(unittest.TestCase):

    def test_is_n_values(self):
        n = exer.MyDict()
        n.a = 1
        self.assertEqual(n.a, 1)
        n.b = 2
        self.assertNotEqual(n.b, 3)

    def test_is_non_values(self):
        n = exer.MyDict()
        n.a = 1
        n.b = 2
        self.assertNotEqual(n.a, 'Bananas')
        self.assertNotEqual(n.b, 'Cherrys')



if __name__ == '__main__':
    unittest.main()

