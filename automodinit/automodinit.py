# automodinit
# Solves the problem of forgetting to keep __init__.py files up to date
# (C) 2012 Niall Douglas http://www.nedproductions.biz/
# See http://pypi.python.org/pypi/automodinit for latest version
# Go to http://github.com/ned14/automodinit to report bugs

import os, pkgutil, sys, inspect

def automodinit(fullmodulename, initfilepath, _g, filter=None, importFindings=True):
    if os.sep+'__init__.py' not in initfilepath: raise Exception, "'"+initfilepath+"' not an __init__ file"
    modulepath=os.path.dirname(initfilepath)
    modulecontents=[x for x in pkgutil.iter_modules([modulepath])]

    if filter is not None: modulecontents=filter(modulecontents)
    
    # Rewrite myself with the updated list
    modulefiles=[x[1] for x in modulecontents]
    if _g['__all__']!=modulefiles:
        initfilepath2=initfilepath[:-1] if initfilepath[-3:]!='.py' else initfilepath
        if os.path.exists(initfilepath2):
            # This may fail if running inside a ZIP file
            badmagic=False
            try:
                with open(initfilepath2, 'rU+') as meh:
                    myself=meh.read()
                    insertpoint=myself.find("# Don't modify the line above, or this line!")
                    if insertpoint==-1:
                        badmagic=True
                        raise Exception, "Calling file missing magic modify line"
                    newmyself='__all__ = '+repr(modulefiles)+'\n'
                    newmyself+=myself[insertpoint:]
                    meh.seek(0)
                    meh.write(newmyself)
                    meh.truncate()
            except:
                if badmagic: raise
        # Fix myself up to have the correct __all__
        _g['__all__']=modulefiles

    if importFindings:
        for loader, modulename, ispkg in modulecontents:
            fullmodulename2=fullmodulename+'.'+modulename            
            #print fullmodulename2, "Already loaded=",fullmodulename2 in sys.modules
            if fullmodulename2 in sys.modules:
                module=sys.modules[fullmodulename2]
            else:
                module=loader.find_module(fullmodulename2).load_module(fullmodulename2)
            _g[modulename]=module
            