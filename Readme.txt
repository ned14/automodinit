automodinit v0.12 5th March 2011:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Niall Douglas http://www.nedproductions.biz/
See http://pypi.python.org/pypi/automodinit for latest version
Go to http://github.com/ned14/automodinit to report bugs

Is this the smallest package on Pypi? That I have no idea, but it fixes
a small problem which has been bugging me throughout years of python
development: forgetting to keep a module's __init__.py up to date with
new files added. This causes the following, irritating problems:

1. Test suites don't find docstring tests.
2. Static analysis tools don't see some module content in __all__.
3. Things which scan themselves for plugins mismatch what os.listdir()
   returns as against what the module import table has.
4. I waste time over something which should take care of itself.
5. os.listdir() based solutions tend to fail when freezed into
   an executable binary because they don't understand running from
   inside a ZIP archive.
   
So here's how to make the problem go away forever:
 
1. Include the automodinit package into your setup.py dependencies.
2. Replace all __init__.py files like this:
 
__all__ = ["I will get rewritten"]
# Don't modify the line above, or this line!
import automodinit
automodinit.automodinit(__name__, __file__, globals())
del automodinit
# Anything else you want can go after here, it won't get modified.

3. That's it! From now on importing a module will set __all__ to
   a list of .py[co] files in the module and will also import each
   of those files as though you had typed:
   
   for x in __all__: import x
   
   Therefore the effect of "from M import *" matches exactly "import M".
   
Customising:
-=-=-=-=-=-=
automodinit can take the following additional parameters:

filter: This is a callable which will be passed a list of tuples
        (loader, modulename, ispkg) which is the output of
        pkgutil.iter_modules() for the calling module. Return only
        those which you want to be imported.
importFindings: Defaults to True. Set to False to not auto-import
                the contents of __all__.

Version history:
-=-=-=-=-=-=-=-=
 * v0.12 5th Mar 2012
   * Fixed a bug where isinstance would occasionally fail. Turns out the
pkgutil loading mechanism doesn't check to see if the module is already
loaded, so it was loading duplicates whose types wouldn't compare.

 * v0.11 5th Mar 2012
   * Fixed some typos in Readme.txt
   * Typically what worked before packaging did not work after. Fixed!

 * v0.10 5th Mar 2012
   First release
