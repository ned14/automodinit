__all__ = ['automodinit', 'foo']
# Don't modify the line above, or this line!
from automodinit import automodinit as ami
ami(__name__, __file__, globals())
automodinit=ami

# automodinit
# Solves the problem of forgetting to keep __init__.py files up to date
# (C) 2012 Niall Douglas http://www.nedproductions.biz/
# See http://pypi.python.org/pypi/automodinit for latest version
# Go to http://github.com/ned14/automodinit to report bugs
