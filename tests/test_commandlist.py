import unittest
from ambrosio import commandlist

class TestCommandList(unittest.TestCase):

    def test_000_newqueue_length(self):
        cl = commandlist.CommandList()
        self.assertEqual(cl.length(),0)

    def test_001_newqueue_cantpop(self):
        cl = commandlist.CommandList()
        self.assertRaises(IndexError,cl.next)

    def test_002_push_then_pop(self):
        cl = commandlist.CommandList()
        cl.append("Test")
        c = cl.next()
        self.assertEqual(c,"Test")

if __name__ == "__main__":
    import sys
    sys.exit(unittest.main())
