# automodinit
# Solves the problem of forgetting to keep __init__.py files up to date
# (C) 2012 Niall Douglas http://www.nedproductions.biz/
# See http://pypi.python.org/pypi/automodinit for latest version
# Go to http://github.com/ned14/automodinit to report bugs


import unittest, zipfile, os, sys

class TestInsideZip(unittest.TestCase):
    def setUp(self):
        with zipfile.ZipFile('test.zip', 'w') as oh:
            for dirpath, dirnames, filenames in os.walk("automodinit"):
                zipdirpath="automodinit_zip"+dirpath[11:]
                for filename in filenames:
                    oh.write(os.path.join(dirpath, filename), zipdirpath+'/'+filename)
        sys.path.insert(0, 'test.zip')
    
    def tearDown(self):
        del sys.path[0]
        os.remove('test.zip')
        
    def test(self):
        import automodinit_zip
        self.assertTrue('foo' in automodinit_zip.__all__)
        self.assertTrue(6==automodinit_zip.foo.foo(5))

if __name__=="__main__":
    unittest.main()
    