import unittest
from array_list import ArrayList

class TestArrayList(unittest.TestCase):
    def test_append_and_length(self):
        lst = ArrayList()
        lst.append('a')
        lst.append('b')
        self.assertEqual(lst.length(), 2)

    def test_insert(self):
        lst = ArrayList()
        lst.append('a')
        lst.insert('b', 1)
        self.assertEqual(str(lst), 'ab')

    def test_delete(self):
        lst = ArrayList()
        lst.append('x')
        self.assertEqual(lst.delete(0), 'x')
        self.assertEqual(lst.length(), 0)

    def test_clone(self):
        lst = ArrayList()
        lst.append('z')
        copy = lst.clone()
        self.assertEqual(str(copy), 'z')
    
    def test_fail_example(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
