import unittest
import automodinit

class TestNormal(unittest.TestCase):
    def test(self):
        self.assertTrue('foo' in automodinit.__all__)
        self.assertTrue(6==automodinit.foo.foo(5))

if __name__=="__main__":
    unittest.main()
    