# py2exe download link: http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
# grab py2exe installer with this setup.py file and create new folder for instance Toexe

from distutils.core import setup
import py2exe , sys, os



sys.argv.append("py2exe")
setup(
    options = {'py2exe': {'bundle_files': 1}},
 
    windows = [{'script': "service.py"}],    #change service.py to your python file name
    zipfile = None,
    
)
