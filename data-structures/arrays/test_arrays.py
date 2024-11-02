import unittest
from .static_array import StaticArray

class TestStaticArrays(unittest.TestCase):

    def test_len(self):
        array = StaticArray(10)
        self.assertEqual(10, len(array))

class TestDynamicArrays(unittest.TestCase):

    pass

if __name__ == "__main__":
    unittest.main()
